import re
import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATASET_PATH = PROJECT_ROOT / "datasets" / "WA_Fn-UseC_-HR-Employee-Attrition.csv"

df = pd.read_csv(DATASET_PATH)

# normalizing column name from camelCase to snake_case
df.columns = [re.sub(r'(?<!^)(?=[A-Z])', '_', col).lower() for col in df.columns]

string_columns = df.select_dtypes(include=["object", "string"]).columns

df[string_columns] = df[string_columns].apply(lambda col: col.str.lower().str.strip())

# check the column name and values that we want to achieve ? 
print(df.columns)
print(df.head(20))

# target feature is attrition  -> meaning removal of employee from company we have to classify employees who is likely to leave company 

# one row represent a employee we have a total of 1470 and 35 features -> 34 x and 1 y 

# ['age',  
# 'attrition', -> will leave or not 
#  'business_travel', -> how much travel have an employee make to go office
#  'daily_rate',  -> 
#  'department', 
#  'distance_from_home', -> 
#  'education',
#  'education_field',
#  'employee_count',
#  'employee_number',
#  'environment_satisfaction',
#  'gender',
#  'hourly_rate',
#  'job_involvement',
#  'job_level',
#  'job_role',
#  'job_satisfaction',
#  'marital_status',
#  'monthly_income', 
#  'monthly_rate',
#  'num_companies_worked',
#  'over18',
#  'over_time',
#  'percent_salary_hike',
#  'performance_rating',
#  'relationship_satisfaction',
#  'standard_hours',
#  'stock_option_level',
#  'total_working_years',
#  'training_times_last_year',
#  'work_life_balance',
#  'years_at_company',
#  'years_in_current_role',
#  'years_since_last_promotion',
#  'years_with_curr_manager'],


print(df[["employee_count", "over18", "standard_hours"]])

print(df["over18"].nunique())

print(df["employee_count"].nunique())

print(df["standard_hours"].nunique())

# data cleaning

# we dropped this columns because we do not need any columns with constant value.
df.drop(
    columns =[
    "over18",
    "employee_count",
    "standard_hours"],
    inplace= True
)

# employee number is a unique identifier(like primary in Database) not a feature 

print(df["employee_number"].nunique())

print(df["age"].min())
print(df["age"].max())

# DATA VALIDATION
# check valid age of employees

invalid_age = df[df["age"] > 60]
print(invalid_age)

# check is there is any one who is doing Unpaid internships
invalid_salary = df[df["monthly_income"] == 0]
print(invalid_salary)

# check invalid distance
invalid_distance = df[df["distance_from_home"] < 0]
print(invalid_distance)

# check invalid experience
invalid_experience = df[df["years_at_company"] > df["total_working_years"]]
print(invalid_experience)

# check for invalid roles means working year company is more than years in curr role in same company, practically not possible
invalid_role = df[df["years_in_current_role"] > df["years_at_company"]]
print(invalid_role)


# check for promotion 
invalid_promotion = df[df["years_since_last_promotion"] > df["years_at_company"]]
print(invalid_promotion)

# check current manager, check years with curr manager is greater than years at company 
invalid_manager = df[df["years_with_curr_manager"] > df["years_at_company"]]
print(invalid_manager)

invalid_company_count = df[(df["total_working_years"]) <= 0 & (df["num_companies_worked"] > 0)]
print(invalid_company_count)

invalid_rating = df[~df["performance_rating"].isin([3, 4])]
print(invalid_rating)

# EXPLORATORY DATA ANALYSIS
print(df["attrition"].value_counts())

print(df["attrition"].value_counts(normalize=True) * 100)

# groupby returns pandas object
# groupby returns a DataFrameGroupBy object.
# think of it like that we have done grouping now we will get the number

# number of employees who had left the company and the percentage left
left_employee = df[df["attrition"] == "yes"]
print(left_employee)
department_groups = df.groupby("department")
print(department_groups)

print(df.groupby("department").size())

total_employees = df.groupby("department").size()
left_employees = df[df["attrition"] == "yes"].groupby("department").size()
attrition_rate = ((left_employees/total_employees)*100).sort_values(ascending=False)

print(attrition_rate)
print(df.columns)
print(df[["monthly_income", "over_time"]])

# In sales department how many left due to overtime ? 
sales_df = df[df["department"] == "sales"]
total_sales = sales_df.groupby("over_time").size()
left_sales = (
    sales_df[sales_df["attrition"] == "yes"]
    .groupby("over_time")
    .size()
)

sales_attrition_rate = (left_sales / total_sales) * 100

print(sales_attrition_rate)
# [1470 rows x 2 columns]
# over_time
# no     13.836478
# yes    37.500000
# dtype: float64
# conclusion is, sales is getting affected due to overtime. 

# how much attrition rate is  there due to over_time ? 
over_time_df = df[df["over_time"] == "yes"]
print(over_time_df["attrition"].head())
total_over_time_employees = len(over_time_df)

left_over_time = len(
    over_time_df[
        over_time_df["attrition"] == "yes"
    ]
)
left_rate = (left_over_time/total_over_time_employees)*100
print(left_rate)
# Name: attrition, dtype: str
# 30.528846153846157

# 4. Does monthly income affect attrition?
# features to use, so that i can answer the question 
# monthly_income 
# stock_option_level

print(df["monthly_income"].describe())