import pandas as pd
from pathlib import Path

print("Script started")

# Path to your dat file
dat_file = Path(r"C:\Users\awoye\Finance_data_analysis_project\project-data\eda_raw_db\3314.dat")

print("Checking dat file...")
print("Dat file path:", dat_file)
print("Dat file exists:", dat_file.exists())

# Output CSV location
output_file = Path("data/loan_payments.csv")

print("CSV will save to:", output_file.resolve())

# Make sure data folder exists
output_file.parent.mkdir(parents=True, exist_ok=True)

# Load the dat file
print("Loading dat file...")
df = pd.read_csv(dat_file, sep="\t", header=None)

print("Saving CSV...")
df.to_csv(output_file, index=False)

print("CSV created successfully")
print("Shape:", df.shape)
print(df.head())
