import sqlite3
import pandas as pd

# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("health_data.db")

# Load CSV
df = pd.read_csv("data/final_integrated_health_data.csv")


# Load into database table
df.to_sql("Fact_Health", conn, if_exists="replace", index=False)

print("Data loaded into SQLite successfully!")

conn.close()
