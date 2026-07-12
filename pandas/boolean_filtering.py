import pandas as pd
from pathlib import Path
# import numpy as np

# after this do one thing all the entries in DB if its string convert it to lower case and columns name should be in format
# word1_word2 -> example MonthlyIncome -> monthly_income and Monthly income -> monthly_income
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATASET_PATH = PROJECT_ROOT / "datasets" / "WA_Fn-UseC_-HR-Employee-Attrition.csv"

df = pd.read_csv(DATASET_PATH)
print(df.columns)
print(df[df["Age"] > 40])

# and operator 
# separate conditions using bracket always 
print(df[
        (df["Age"] > 40) &
        (df["MonthlyIncome"] > 10000)
])

print(df[
        (df["Department"] == "Sales") |
        (df["Department"] == "Human Resources")
])

print(df[
    ~(df["OverTime"] == "Yes")
])
# above and below both the things are same
print(df[
    df["OverTime"] != "Yes"
])

# filter and selecting column at the same time 
print(df.loc[
    df["Age"] > 40,
    ["Age", "MonthlyIncome", "Department"]
])

# isin() in pandas 
print(df[
    df["Department"].isin(["Sales", "Human Resources"])
])

# between() in pandas 

print(df[
    df["Age"].between(30,40)
])

# string filering

print(df[
    df["JobRole"].str.contains("Manager")
])

print(df[
    df["JobRole"].str.startswith("Sales")
])

print(df[
    df["JobRole"].str.endswith("Manager")
])

# if data set contains null values we should know before hand before doing this 
print(df[
    df["MonthlyIncome"].isna()
])

print(df[
    df["MonthlyIncome"].notna()
])

# if we want to use raw query in this 
print(
    df.query(
        "Age > 40 and MonthlyIncome > 10000"
    )
)

# filtering based on variables 
age = 40
salary = 10000

print(df[
    (df["Age"] > age) &
    (df["MonthlyIncome"] > salary)
])

high_salary = df[df["MonthlyIncome"] > 10000]

print(len(high_salary))

print(df[
    df["Department"] == "Sales"
].sort_values(
    by = "MonthlyIncome",
    ascending=False
))

df[
    df["Department"] == "Sales"
].nlargest(
    5,
    "MonthlyIncome"
)

# Things to Remember


# Always wrap each condition in parentheses:
# (condition1) & (condition2)
# Use:
# & → AND
# | → OR
# ~ → NOT
# Never use and, or, not with Pandas Series.
# Use loc when you want specific columns after filtering.
# Prefer isin() over multiple OR conditions.
# Prefer between() for range checks.
# Use query() only if you find it more readable; standard boolean masking is more common in production code.