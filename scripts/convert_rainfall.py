from pathlib import Path

import numpy as np
import pandas as pd
import xarray as xr
import geopandas as gpd
from shapely.geometry import Point


# ============================================================
# 1. PATHS
# ============================================================

RAINFALL_DIR = Path("data/raw/rainfall")
BOUNDARY_FILE = Path("data/raw/basin_boundaries/Subbasin.shp")
OUTPUT_DIR = Path("data/interim")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# 2. READ BASIN BOUNDARIES
# ============================================================

print("Reading basin boundaries...")

basins = gpd.read_file(BOUNDARY_FILE)

print("\nAvailable columns:")
print(basins.columns)

print("\nOriginal CRS:")
print(basins.crs)


# ============================================================
# 3. SELECT KRISHNA AND CAUVERY
# ============================================================

krishna = basins[
    basins["ba_name"] == "Krishna Basin"
].copy()

cauvery = basins[
    basins["ba_name"] == "Cauvery Basin"
].copy()


print("\nKrishna sub-basins:")
print(
    krishna[
        ["sub_basin", "sbcode", "bacode"]
    ].to_string(index=False)
)

print("\nCauvery sub-basins:")
print(
    cauvery[
        ["sub_basin", "sbcode", "bacode"]
    ].to_string(index=False)
)


# ============================================================
# 4. CHECK THAT WE FOUND THE BASINS
# ============================================================

if krishna.empty:
    raise ValueError("Krishna Basin was not found in the shapefile.")

if cauvery.empty:
    raise ValueError("Cauvery Basin was not found in the shapefile.")


# ============================================================
# 5. CONVERT BASIN CRS TO LAT/LONG
# ============================================================
#
# Your rainfall NetCDF uses:
#
# LATITUDE
# LONGITUDE
#
# These are geographic coordinates.
#
# EPSG:4326 = WGS84 latitude/longitude.
# ============================================================

krishna = krishna.to_crs("EPSG:4326")
cauvery = cauvery.to_crs("EPSG:4326")

print("\nConverted basin CRS:")
print(krishna.crs)


# ============================================================
# 6. COMBINE ALL SUB-BASINS
# ============================================================
#
# Krishna may contain several sub-basin polygons.
#
# Cauvery contains:
#   - Cauvery Upper
#   - Cauvery Middle
#   - Cauvery Lower
#
# union_all() combines them into one geometry.
# ============================================================

krishna_geometry = krishna.geometry.union_all()
cauvery_geometry = cauvery.geometry.union_all()

print("\nKrishna geometry created.")
print("Cauvery geometry created.")


# ============================================================
# 7. FIND ALL NETCDF FILES
# ============================================================

rainfall_files = sorted(
    RAINFALL_DIR.glob("*.nc")
)

if not rainfall_files:
    raise FileNotFoundError(
        f"No .nc files found in {RAINFALL_DIR}"
    )

print(f"\nFound {len(rainfall_files)} rainfall files.")

for file in rainfall_files:
    print(f"  - {file.name}")


# ============================================================
# 8. PROCESS EACH NETCDF FILE
# ============================================================

krishna_results = []
cauvery_results = []


for rainfall_file in rainfall_files:

    print("\n" + "=" * 60)
    print(f"Processing: {rainfall_file.name}")
    print("=" * 60)

    # --------------------------------------------------------
    # Open NetCDF
    # --------------------------------------------------------

    ds = xr.open_dataset(rainfall_file)

    print(ds)

    # --------------------------------------------------------
    # Get rainfall variable
    # --------------------------------------------------------

    rainfall = ds["RAINFALL"]

    print("\nRainfall attributes:")
    print(rainfall.attrs)

    # --------------------------------------------------------
    # Get coordinates
    # --------------------------------------------------------

    latitudes = ds["LATITUDE"].values
    longitudes = ds["LONGITUDE"].values

    print(
        f"\nLatitude range: "
        f"{latitudes.min()} to {latitudes.max()}"
    )

    print(
        f"Longitude range: "
        f"{longitudes.min()} to {longitudes.max()}"
    )

    # --------------------------------------------------------
    # Create latitude/longitude grid
    # --------------------------------------------------------
    #
    # Example:
    #
    # latitude:
    #   10, 10.25, 10.5
    #
    # longitude:
    #   74, 74.25, 74.5
    #
    # meshgrid creates every possible pair.
    # --------------------------------------------------------

    lon_grid, lat_grid = np.meshgrid(
        longitudes,
        latitudes
    )

    # Flatten the grid
    flat_lats = lat_grid.ravel()
    flat_lons = lon_grid.ravel()

    # --------------------------------------------------------
    # Create GeoDataFrame containing every rainfall point
    # --------------------------------------------------------

    points = gpd.GeoDataFrame(
        {
            "latitude": flat_lats,
            "longitude": flat_lons,
        },
        geometry=[
            Point(lon, lat)
            for lon, lat in zip(
                flat_lons,
                flat_lats
            )
        ],
        crs="EPSG:4326"
    )

    # --------------------------------------------------------
    # Find points inside Krishna
    # --------------------------------------------------------

    krishna_mask = points.geometry.within(
        krishna_geometry
    ).values

    # --------------------------------------------------------
    # Find points inside Cauvery
    # --------------------------------------------------------

    cauvery_mask = points.geometry.within(
        cauvery_geometry
    ).values

    print(
        f"\nKrishna rainfall grid points: "
        f"{krishna_mask.sum()}"
    )

    print(
        f"Cauvery rainfall grid points: "
        f"{cauvery_mask.sum()}"
    )

    # --------------------------------------------------------
    # Make sure we actually found points
    # --------------------------------------------------------

    if krishna_mask.sum() == 0:
        raise ValueError(
            "No rainfall grid points found inside Krishna Basin."
        )

    if cauvery_mask.sum() == 0:
        raise ValueError(
            "No rainfall grid points found inside Cauvery Basin."
        )

    # --------------------------------------------------------
    # Reshape masks back to rainfall grid
    # --------------------------------------------------------

    krishna_mask_2d = krishna_mask.reshape(
        len(latitudes),
        len(longitudes)
    )

    cauvery_mask_2d = cauvery_mask.reshape(
        len(latitudes),
        len(longitudes)
    )

    # --------------------------------------------------------
    # Apply masks
    # --------------------------------------------------------

    krishna_rainfall = rainfall.where(
        krishna_mask_2d
    )

    cauvery_rainfall = rainfall.where(
        cauvery_mask_2d
    )

    # --------------------------------------------------------
    # Calculate spatial average for every day
    # --------------------------------------------------------
    #
    # We average over:
    #
    # LATITUDE
    # LONGITUDE
    #
    # TIME remains.
    # --------------------------------------------------------

    krishna_daily = krishna_rainfall.mean(
        dim=["LATITUDE", "LONGITUDE"],
        skipna=True
    )

    cauvery_daily = cauvery_rainfall.mean(
        dim=["LATITUDE", "LONGITUDE"],
        skipna=True
    )

    # --------------------------------------------------------
    # Convert to pandas DataFrames
    # --------------------------------------------------------

    krishna_df = krishna_daily.to_dataframe(
        name="rainfall"
    ).reset_index()

    cauvery_df = cauvery_daily.to_dataframe(
        name="rainfall"
    ).reset_index()

    # --------------------------------------------------------
    # Keep only useful columns
    # --------------------------------------------------------

    krishna_df = krishna_df[
        ["TIME", "rainfall"]
    ]

    cauvery_df = cauvery_df[
        ["TIME", "rainfall"]
    ]

    # --------------------------------------------------------
    # Rename date column
    # --------------------------------------------------------

    krishna_df.rename(
        columns={"TIME": "date"},
        inplace=True
    )

    cauvery_df.rename(
        columns={"TIME": "date"},
        inplace=True
    )

    # --------------------------------------------------------
    # Add results to list
    # --------------------------------------------------------

    krishna_results.append(krishna_df)

    cauvery_results.append(cauvery_df)

    # --------------------------------------------------------
    # Close NetCDF
    # --------------------------------------------------------

    ds.close()


# ============================================================
# 9. COMBINE ALL YEARS
# ============================================================

krishna_final = pd.concat(
    krishna_results,
    ignore_index=True
)

cauvery_final = pd.concat(
    cauvery_results,
    ignore_index=True
)


# ============================================================
# 10. CLEAN DATA
# ============================================================

krishna_final["date"] = pd.to_datetime(
    krishna_final["date"]
)

cauvery_final["date"] = pd.to_datetime(
    cauvery_final["date"]
)

krishna_final = krishna_final.sort_values(
    "date"
).reset_index(drop=True)

cauvery_final = cauvery_final.sort_values(
    "date"
).reset_index(drop=True)


# ============================================================
# 11. SAVE CSV FILES
# ============================================================

krishna_output = (
    OUTPUT_DIR / "krishna_rainfall.csv"
)

cauvery_output = (
    OUTPUT_DIR / "cauvery_rainfall.csv"
)

krishna_final.to_csv(
    krishna_output,
    index=False
)

cauvery_final.to_csv(
    cauvery_output,
    index=False
)


# ============================================================
# 12. PRINT RESULTS
# ============================================================

print("\n" + "=" * 60)
print("DONE")
print("=" * 60)

print(
    f"\nKrishna rainfall saved to:"
    f"\n{krishna_output}"
)

print(
    f"\nCauvery rainfall saved to:"
    f"\n{cauvery_output}"
)

print(
    f"\nKrishna records: "
    f"{len(krishna_final)}"
)

print(
    f"Cauvery records: "
    f"{len(cauvery_final)}"
)

print("\nKrishna rainfall:")
print(krishna_final.head())

print("\nCauvery rainfall:")
print(cauvery_final.head())