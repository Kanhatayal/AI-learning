# Problem 2: Data Cleaning

# You'll notice:

# duplicate values
# categorical values
# inconsistent formats

# This naturally motivates Pandas.

# DATA CLEANING KIND, WE ARE LOOKING FOR MISSING VALUES, DUPLICATE VALUES,  

import pandas as pd
import numpy as np
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
print(PROJECT_ROOT)
DATASET_PATH = PROJECT_ROOT / "datasets" / "WA_Fn-UseC_-HR-Employee-Attrition.csv"
print(DATASET_PATH)
df = pd.read_csv(DATASET_PATH)

features = [
    "Age",
    "MonthlyIncome",
    "YearsAtCompany",
    "PerformanceRating",
    "DistanceFromHome",
    "PercentSalaryHike"
]

employee_data = df[features].to_numpy()

print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.dtypes)

print(df["Department"].unique())
print(df["JobRole"].unique())
print(df["OverTime"].unique())

print(df["Age"].min())
print(df["Age"].max())

print(df["MonthlyIncome"].describe())