import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("health_data.db")

# 1️⃣ Trend Analysis - Maternal Mortality
query1 = """
SELECT Country, Year, Value
FROM Fact_Health
WHERE Indicator = 'Maternal Mortality'
ORDER BY Country, Year;
"""

df1 = pd.read_sql(query1, conn)
print("\nMaternal Mortality Trend Sample:")
print(df1.head())


# 2️⃣ Compare Indicators Same Year
query2 = """
SELECT f1.Country, f1.Year,
       f1.Value AS Maternal_Mortality,
       f2.Value AS Health_Expenditure
FROM Fact_Health f1
JOIN Fact_Health f2
  ON f1.Country = f2.Country
 AND f1.Year = f2.Year
WHERE f1.Indicator = 'Maternal Mortality'
AND f2.Indicator = 'Health Expenditure % GDP'
ORDER BY f1.Country, f1.Year;
"""

df2 = pd.read_sql(query2, conn)
print("\nComparison Sample:")
print(df2.head())


# 3️⃣ Data Validation Checks
query3 = """
SELECT COUNT(*) AS Null_Count
FROM Fact_Health
WHERE Value IS NULL;
"""

df3 = pd.read_sql(query3, conn)
print("\nNull Check:")
print(df3)

conn.close()
