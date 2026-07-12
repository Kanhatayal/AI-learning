# Create new features like:

# ExperienceRatio = YearsAtCompany / TotalWorkingYears

# or

# IncomePerYear = MonthlyIncome / TotalWorkingYears

# This is what ML engineers actually do before training models.

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

# check for invalid rows 
invalid_rows = df[
    (df["TotalWorkingYears"] == 0) &
    (
        (df["YearsAtCompany"] > 0) |
        (df["NumCompaniesWorked"] > 0)
    )
]

print(invalid_rows)

df["ExperienceRatio"] = (
    df["YearsAtCompany"] /
    df["TotalWorkingYears"]
)

print(df[
    [
        "YearsAtCompany",
        "TotalWorkingYears",
        "ExperienceRatio"
    ]
].head())

# ANNUAL INCOME FEATURE INTRODUCED 
df["AnnualIncome"] = df["MonthlyIncome"] * 12

print(df[
    [
        "MonthlyIncome",
        "AnnualIncome"
    ]
].head())