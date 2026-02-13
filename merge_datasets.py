import pandas as pd

# Load World Bank data
wb_df = pd.read_csv("data/processed_health_data.csv")

# Load WHO cleaned data
who_df = pd.read_csv("data/cleaned_who_data.csv")

# Combine both datasets
final_df = pd.concat([wb_df, who_df], ignore_index=True)

# Save final integrated dataset
final_df.to_csv("data/final_integrated_health_data.csv", index=False)

print("World Bank + WHO data merged successfully!")
