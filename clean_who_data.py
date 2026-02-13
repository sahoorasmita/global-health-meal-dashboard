import pandas as pd

# Load WHO file
df = pd.read_csv("data/who_skilled_birth.csv")

# Keep only required columns
df = df[["GEO_NAME_SHORT", "DIM_TIME", "RATE_PER_100_N"]]

# Rename columns to match World Bank format
df.columns = ["Country", "Year", "Value"]

# Extract proper year (handles values like 1999-2000)
df["Year"] = df["Year"].astype(str)
df["Year"] = df["Year"].str[:4]
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")

# Convert Value column to numeric
df["Value"] = pd.to_numeric(df["Value"], errors="coerce")

# Remove null values
df.dropna(subset=["Year", "Value"], inplace=True)

# Add Indicator column
df["Indicator"] = "Skilled Birth Attendance (%)"

# Add CountryCode column (leave blank for now)
df["CountryCode"] = None

# Reorder columns to match World Bank dataset
df = df[["Country", "CountryCode", "Year", "Value", "Indicator"]]

# Save cleaned file
df.to_csv("data/cleaned_who_data.csv", index=False)

print("WHO data cleaned successfully!")
