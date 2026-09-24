import pandas as pd

krishna_tmax = pd.read_csv("data/interim/krishna_tmax_2001_2025.csv")
krishna_tmin = pd.read_csv("data/interim/krishna_tmin_2001_2025.csv")
kaveri_tmax = pd.read_csv("data/interim/kaveri_tmax_2001_2025.csv")
kaveri_tmin = pd.read_csv("data/interim/kaveri_tmin_2001_2025.csv")

print("Krishna Tmax:-")
print(krishna_tmax.head())
print("Krishna Tmin:-")
print(krishna_tmin.head())
print("Kaveri Tmax:-")
print(kaveri_tmax.head())
print("Kaveri Tmin:-")
print(kaveri_tmin.head())