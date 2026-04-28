# 🌍 Climate Data Analysis Project

## 📌 Overview

This project performs climate data analysis using datasets from multiple countries. It includes data cleaning, exploratory data analysis (EDA), and cross-country comparison to assess climate patterns and vulnerability.


🎯 Objectives

* Clean and preprocess raw climate data
* Perform exploratory data analysis (EDA)
* Compare multiple countries
* Rank countries based on climate vulnerability
* Build a reusable data processing pipeline


📂 Project Structure

```
climate-challenge-week0/
│
├── data/                  # Raw and processed data (ignored by Git)
├── notebooks/             # Jupyter notebooks for EDA and analysis
│   ├── ethiopia_eda.ipynb
│   └── multi_country_analysis.ipynb
│
├── scripts/               # Reusable Python scripts
│   └── climate_analysis.py
│
├── .gitignore
├── README.md
└── requirements.txt
```


⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd climate-challenge-week0
```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate environment

**Windows (Git Bash):**

```bash
source venv/Scripts/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```


▶️ Running the Project

### Run the data processing script

```bash
python scripts/climate_analysis.py data data/output.csv
```

### Run notebooks

Open in VS Code and execute:

* `ethiopia_eda.ipynb`
* `multi_country_analysis.ipynb`


🧹 Data Cleaning Steps

* Replaced invalid values (`-999`) with NaN
* Removed duplicate rows
* Converted `YEAR` and `DOY` into datetime
* Extracted `Month`
* Handled missing values using forward fill
* Removed outliers using Z-score


📊 Analysis Performed

### Single Country (EDA)

* Summary statistics
* Missing value analysis
* Time series trends
* Correlation analysis
* Distribution analysis

### Multi-Country Analysis

* Aggregated climate metrics per country
* Cross-country comparison (temperature, rainfall, humidity)
* Visualization of differences


⚠️ Climate Vulnerability Ranking

A vulnerability score was computed using:

* Temperature (T2M)
* Precipitation (PRECTOTCORR)
* Humidity (RH2M)

Countries were ranked based on a weighted combination of these factors.


🛡️ Error Handling

* File loading wrapped in try/except
* Invalid files skipped safely
* Logging used for transparency


📦 Dependencies

* pandas
* numpy
* matplotlib
* seaborn
* scipy


🚫 Notes

* The `data/` folder is excluded using `.gitignore`
* CSV files are not pushed to GitHub


✅ Status

✔ Task 1: Environment setup
✔ Task 2: Data cleaning and EDA
✔ Task 3: Multi-country analysis and ranking
✔ Bonus: CLI arguments and logging


