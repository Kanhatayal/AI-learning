import re
import pandas as pd
from pathlib import Path

# ---------------------------------------------
# Load Dataset
# ---------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATASET_PATH = PROJECT_ROOT / "datasets" / "WA_Fn-UseC_-HR-Employee-Attrition.csv"

df = pd.read_csv(DATASET_PATH)

# ---------------------------------------------
# Convert Column Names
# MonthlyIncome -> monthly_income
# YearsAtCompany -> years_at_company
# ---------------------------------------------

df.columns = [
    re.sub(r'(?<!^)(?=[A-Z])', '_', col).lower()
    for col in df.columns
]

# ---------------------------------------------
# Convert all string values to lowercase
# ---------------------------------------------

string_columns = df.select_dtypes(include=["object", "string"]).columns

df[string_columns] = df[string_columns].apply(
    lambda col: col.str.lower().str.strip()
)

print(df.columns)

# top 10 highly paid employees
print(df.sort_values(
    by= "monthly_income",
    ascending=False
))

# employee with lowest salary 

print(df.sort_values(
    by= "monthly_income"
))

# sorting multiple columns in different fashion 
# Sort by:

# Highest salary
# Highest performance rating

df.sort_values(
    by=["monthly_income", "performance_rating"],
    ascending=[False, False]
)


df.nlargest(
    10,
    "monthly_income"
)

df.nsmallest(
    10,
    "monthly_income"
)

# make a new feature in data set
# highest salary with rank one
df["salary_rank"] = df["monthly_income"].rank(
    ascending= False
)
# in mulitiple employees have same salary 
df["salary_rank"] = df["monthly_income"].rank(
    method="dense",
    ascending=False
)
# avg rank 
df["salary_rank"] = df["monthly_income"].rank()

# percentile rank

df["salary_percentile"] = df["monthly_income"].rank(
    pct=True
)

print(df.columns)

# MINI CHALLENGE ON THIS CHAPTER 

print(df.loc[:,[
    "employee_number",
    "department",
    "job_role",
    "monthly_income",
    "performance_rating"
]].sort_values(
    by= "monthly_income",
    ascending=False
).head(10)
)

# Both produce the same result. The second style is generally preferred because it follows the natural order:
# Filter/Sort → Select Columns → Limit Rows.


print(df.sort_values(
    by="monthly_income",
    ascending=False
).loc[:, [
    "employee_number",
    "department",
    "job_role",
    "monthly_income",
    "performance_rating"
]].head(10)
)