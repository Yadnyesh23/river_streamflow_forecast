from pathlib import Path
import pandas as pd

# -----------------------------
# Paths
# -----------------------------
RAW_DIR = Path("data/raw/streamflow")
OUTPUT_DIR = Path("data/interim")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Krishna basin keywords
TARGET_BASIN = "Krishna"

# Read every state CSV
all_data = []

for file in RAW_DIR.glob("*.csv"):
    print(f"Reading {file.name}")

    df = pd.read_csv(file)  

    # Keep only Krishna basin stations
    df = df[df["Basin"].str.contains(TARGET_BASIN, case=False, na=False)]

    if len(df) == 0:
        continue

    # Select required columns
    df = df[
        [
            "Data Acquisition Time",
            "Station",
            "River",
            "Basin",
            "Latitude",
            "Longitude",
            "Manual Daily River Water Discharge (m3/sec)"
        ]
    ].copy()

    # Rename columns
    df.rename(columns={
        "Data Acquisition Time": "date",
        "Manual Daily River Water Discharge (m3/sec)": "streamflow",
        "Station": "station_name",
        "River": "river"
    }, inplace=True)

    # Convert date
    # Convert DD-MM-YYYY HH:MM to datetime
    df["date"] = pd.to_datetime(
        df["date"],
        format="%d-%m-%Y %H:%M",
        errors="coerce"
    )

    # Keep only the date (remove 09:00 timestamp)
    df["date"] = df["date"].dt.normalize()

    all_data.append(df)

# Merge all Krishna stations
streamflow_df = pd.concat(all_data, ignore_index=True)

# Sort chronologically
streamflow_df = streamflow_df.sort_values("date").reset_index(drop=True)

# Save
output_file = OUTPUT_DIR / "krishna_streamflow.csv"
streamflow_df.to_csv(output_file, index=False)

print(f"\nSaved {len(streamflow_df)} records.")
print(streamflow_df.head())
print("\nStations Found:")
print(streamflow_df["station_name"].unique())