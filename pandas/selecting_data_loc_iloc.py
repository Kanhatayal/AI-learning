import pandas as pd
from pathlib import Path
# import numpy as np
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATASET_PATH = PROJECT_ROOT / "datasets" / "WA_Fn-UseC_-HR-Employee-Attrition.csv"

df = pd.read_csv(DATASET_PATH)

# PROBLEM STATEMENT

# HR asks:
# Show the employee details for Employee ID 100.
# Later they'll ask:

# Show employees from rows 100–200.
print(df.loc[100:200])
# Show only Age and MonthlyIncome.
print(df.loc[:, ["Age", "MonthlyIncome"]])
# Show employees older than 40.
print(df["Age"] > 40)
# Update salary for a specific employee.

# All of these use loc or iloc.

# iloc
# which excludes the last index.
# iloc → Integer Location
# Uses row and column positions.

# first row of dataset
print(df.iloc[0])


# first cell just like matrix location 
print(df.iloc[0,0])


# first five employees 
print(df.iloc[:5])

# first one is included
print(df.iloc[10:21, :4])

# df.loc
# loc includes both ends. 
# loc → Label Location

# Uses row labels and column names.

print(df.loc[:, "Age"])

print(df.loc[:, ["Age", "MonthlyIncome"]])

print(df.loc[10:20])
