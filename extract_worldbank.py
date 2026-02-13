import requests
import pandas as pd

def fetch_worldbank_data(indicator_code, indicator_name):
    url = f"https://api.worldbank.org/v2/country/all/indicator/{indicator_code}?format=json&per_page=20000"
    
    response = requests.get(url)
    data = response.json()
    
    records = []
    
    for item in data[1]:
        records.append({
            "Country": item["country"]["value"],
            "CountryCode": item["country"]["id"],
            "Year": item["date"],
            "Value": item["value"],
            "Indicator": indicator_name
        })
    
    df = pd.DataFrame(records)
    
    # Clean Data
    df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
    df["Value"] = pd.to_numeric(df["Value"], errors="coerce")
    df.dropna(subset=["Value"], inplace=True)
    
    return df


# Fetch two indicators
maternal_df = fetch_worldbank_data("SH.STA.MMRT", "Maternal Mortality")
health_exp_df = fetch_worldbank_data("SH.XPD.CHEX.GD.ZS", "Health Expenditure % GDP")

# Combine datasets
combined_df = pd.concat([maternal_df, health_exp_df], ignore_index=True)

# Save file
combined_df.to_csv("data/processed_health_data.csv", index=False)

print("Data extraction completed successfully!")
