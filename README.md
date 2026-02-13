# global-health-meal-dashboard
Data Associate Assignment – Public Health Indicators Dashboard using World Bank and WHO APIs
📌 Overview

This project demonstrates how publicly available global health data can be integrated and analyzed to support Monitoring, Evaluation, Accountability, and Learning (MEAL) decision-making.

The dashboard contextualizes maternal health outcomes across countries using external development and health indicators. It enables program teams to identify high-need geographies, compare trends over time, and explore relationships between health investment and outcomes.

🎯 Problem Statement

Maternal mortality remains a major public health challenge in many low- and middle-income countries.

Program teams often require reliable external data to:

Understand country-level trends

Compare regional disparities

Identify high-risk geographies

Inform resource allocation decisions

This project builds a proof-of-concept analytical workflow and dashboard to support evidence-based program monitoring.

📊 Data Sources

Data was extracted using public APIs:

World Bank Open Data API

Health Expenditure (% of GDP)

Development indicators

WHO Global Health Observatory (GHO) API

Maternal Mortality Ratio

Skilled Birth Attendance (%)

Time Coverage: 1990 – Most recent available year

⚙️ Methodology & Approach
1️⃣ Data Extraction

Extracted data programmatically using Python

Connected to public APIs

Retrieved indicator data across countries and years

2️⃣ Data Cleaning & Integration

Standardized country names and formats

Handled missing values

Aligned indicators across time periods

Integrated datasets into a unified analytical structure

3️⃣ Data Modeling

Prepared structured dataset for analysis

Created calculated measures (latest year, averages, trends)

Designed model suitable for dashboard analysis

4️⃣ Visualization

Built interactive dashboard in Power BI

Enabled filtering by geography and time

Designed visuals for trend, comparison, and correlation analysis

📈 Dashboard Features

The Power BI dashboard includes:

KPI cards (latest indicator values)

Trend analysis (maternal mortality over time)

Country comparison (bar chart)

Correlation analysis (health expenditure vs mortality)

Geographic distribution (map visualization)

Interactive slicers (country and year filters)

🔎 Key Insights

Countries with higher health expenditure generally demonstrate lower maternal mortality.

Significant regional disparities persist, particularly in Sub-Saharan Africa.

Higher skilled birth attendance is associated with improved maternal health outcomes.

The dashboard supports identification of high-risk geographies for targeted intervention.

👥 Intended Users

MEAL Teams

Program Managers

Policy Analysts

This tool supports data-driven prioritization and strategic investment decisions.

🛠 Setup Instructions

Clone the repository:

git clone https://github.com/sahoorasmita/global-health-meal-dashboard.git


Install required Python libraries:

pip install pandas requests


Run the data extraction script to generate processed dataset.

Open the Power BI dashboard file (.pbix) to explore interactive visualizations.

⚠️ Limitations

Public datasets may contain reporting delays or missing values.

Observed relationships reflect correlation and do not imply causation.

Data availability varies across countries and years.

🚀 Future Enhancements

Integrate GDP and socio-economic indicators

Incorporate program-level performance data

Develop benchmarking and forecasting capabilities

📎 Repository Structure
global-health-meal-dashboard/
│
├── data_extraction.py
├── processed_data.csv
├── dashboard.pbix
├── screenshots/
│   ├── page1.png
│   └── page2.png
└── README.md
