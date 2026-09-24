"""
Extract IMD gridded daily temperature (tmax, tmin) for the Krishna and
Cauvery (Kaveri) river basins, 2001-2025, and save basin-average daily
time series to data/interim/.

Expects:
  - IMD .GRD files named like tmax2001.GRD, tmax2002.GRD, ... , tmin2001.GRD, ...
    (adjust GRD_DIR and the filename pattern below to match what you downloaded)
  - Subbasin.shp with a 'ba_name' column containing 'Krishna Basin' and 'Cauvery Basin'

Output:
  data/interim/krishna_tmax_2001_2025.csv
  data/interim/krishna_tmin_2001_2025.csv
  data/interim/kaveri_tmax_2001_2025.csv
  data/interim/kaveri_tmin_2001_2025.csv
"""

import os
import numpy as np
import pandas as pd
import rioxarray 
import xarray as xr
import geopandas as gpd

# ---------------- CONFIG ----------------
SHAPEFILE_PATH = "data/raw/basin_boundaries/Subbasin.shp"          # path to your shapefile
GRD_DIRS = {                             # one folder per variable
    "tmax": "data/raw/temperature/tmax",
    "tmin": "data/raw/temperature/tmin",
}
OUT_DIR = "data/interim"                 # output folder
START_YEAR = 2001
END_YEAR = 2025
VARIABLES = ["tmax", "tmin"]             # which variables to extract

# IMD grid geometry (1x1 degree, all-India)
LAT = np.arange(7.5, 38.5, 1.0)   # 31 points
LON = np.arange(67.5, 98.5, 1.0)  # 31 points
MISSING_VALUE = 99.9
# -----------------------------------------


def read_imd_grd(filepath, year, var):
    """Read one IMD .GRD binary file into an xarray DataArray."""
    ndays = 366 if pd.Timestamp(year, 12, 31).is_leap_year else 365
    data = np.fromfile(filepath, dtype=np.float32)

    expected = ndays * len(LAT) * len(LON)
    if data.size != expected:
        raise ValueError(
            f"{filepath}: expected {expected} values for {ndays} days, "
            f"got {data.size}. Check file / grid dimensions."
        )

    data = data.reshape(ndays, len(LAT), len(LON))
    data = np.where(data == MISSING_VALUE, np.nan, data)

    dates = pd.date_range(f"{year}-01-01", periods=ndays)
    da = xr.DataArray(
        data, dims=["time", "lat", "lon"],
        coords={"time": dates, "lat": LAT, "lon": LON},
        name=var,
    )
    da = da.rio.write_crs("EPSG:4326")
    da = da.rio.set_spatial_dims(x_dim="lon", y_dim="lat")
    return da


def load_basin_boundaries(shapefile_path):
    """Load, filter, reproject and dissolve Krishna and Cauvery basins."""
    gdf = gpd.read_file(shapefile_path)

    krishna = gdf[gdf["ba_name"] == "Krishna Basin"].to_crs("EPSG:4326").dissolve()
    kaveri = gdf[gdf["ba_name"] == "Cauvery Basin"].to_crs("EPSG:4326").dissolve()

    if krishna.empty:
        raise ValueError("No features matched 'Krishna Basin' in ba_name column.")
    if kaveri.empty:
        raise ValueError("No features matched 'Cauvery Basin' in ba_name column.")

    return {"krishna": krishna, "kaveri": kaveri}


def extract_series(da, basin_gdf, basin_name, var, year):
    """Clip DataArray to basin and return a basin-average daily dataframe."""
    try:
        clipped = da.rio.clip(
            basin_gdf.geometry, basin_gdf.crs, drop=True, all_touched=True
        )
    except Exception as e:
        print(f"  WARNING: clip failed for {basin_name} {var} {year}: {e}")
        return None

    if clipped.sizes.get("lat", 0) == 0 or clipped.sizes.get("lon", 0) == 0:
        print(f"  WARNING: no grid cells found for {basin_name} {var} {year}")
        return None

    avg = clipped.mean(dim=["lat", "lon"], skipna=True)
    df = avg.to_dataframe(name=var).reset_index()[["time", var]]
    return df


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    basins = load_basin_boundaries(SHAPEFILE_PATH)

    # accumulate results across years, per basin per variable
    results = {basin: {var: [] for var in VARIABLES} for basin in basins}

    for var in VARIABLES:
        var_dir = GRD_DIRS[var]
        for year in range(START_YEAR, END_YEAR + 1):
            filepath = os.path.join(var_dir, f"{year}.GRD")
            if not os.path.exists(filepath):
                print(f"SKIP: {filepath} not found")
                continue

            print(f"Processing {var} {year} ...")
            try:
                da = read_imd_grd(filepath, year, var)
            except Exception as e:
                print(f"  ERROR reading {filepath}: {e}")
                continue

            for basin_name, basin_gdf in basins.items():
                df = extract_series(da, basin_gdf, basin_name, var, year)
                if df is not None:
                    results[basin_name][var].append(df)

    # concatenate and save
    for basin_name in basins:
        for var in VARIABLES:
            if not results[basin_name][var]:
                print(f"No data collected for {basin_name} {var} — skipping save.")
                continue
            combined = pd.concat(results[basin_name][var], ignore_index=True)
            combined = combined.sort_values("time").reset_index(drop=True)

            out_path = os.path.join(
                OUT_DIR, f"{basin_name}_{var}_{START_YEAR}_{END_YEAR}.csv"
            )
            combined.to_csv(out_path, index=False)
            print(f"Saved {out_path}  ({len(combined)} rows)")


if __name__ == "__main__":
    main()