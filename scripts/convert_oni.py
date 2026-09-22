from pathlib import Path
import pandas as pd

# -----------------------------
# Paths
# -----------------------------
RAW_FILE = Path("data/raw/oni/oni.ascii.txt")
OUTPUT_FILE = Path("data/interim/oni.csv")

# Create output folder if it doesn't exist
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

# -----------------------------
# Read NOAA ASCII file
# -----------------------------
oni_df = pd.read_csv(
    RAW_FILE,
    sep=r"\s+",        # split on whitespace
    engine="python"
)

# Keep only required columns
oni_df = oni_df[["SEAS", "YR", "ANOM"]]

# -----------------------------
# Convert seasonal code to month
# -----------------------------
season_to_month = {
    "DJF": 1,
    "JFM": 2,
    "FMA": 3,
    "MAM": 4,
    "AMJ": 5,
    "MJJ": 6,
    "JJA": 7,
    "JAS": 8,
    "ASO": 9,
    "SON": 10,
    "OND": 11,
    "NDJ": 12,
}

oni_df["month"] = oni_df["SEAS"].map(season_to_month)

# Create monthly date (1st day of each month)
oni_df["date"] = pd.to_datetime(
    dict(year=oni_df["YR"], month=oni_df["month"], day=1)
)

# Final dataframe
oni_df = oni_df[["date", "ANOM"]].rename(columns={"ANOM": "oni"})

# Save CSV
oni_df.to_csv(OUTPUT_FILE, index=False)

print(f"Saved {len(oni_df)} rows to {OUTPUT_FILE}")
print(oni_df.head())