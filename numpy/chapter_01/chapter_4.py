import pandas as pd
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

# everything is zero based indexing 
# print that row only 
# 0th row
print(employee_data[0])
# [  41 5993    6    3    1   11]
# 1st row /

print(employee_data[1])
# [  49 5130   10    4    8   23]

# /feature[:column to select]
print(employee_data[:3])
# [[  41 5993    6    3    1   11]
#  [  49 5130   10    4    8   23]
#  [  37 2090    0    3    2   15]]

# print only single column 
print(employee_data[:,0])
# [41 49 37 ... 27 49 34]

# features[:number of rows, column to select]
print(employee_data[:10,0])
# [41 49 37 33 27 32 59 30 38 36]

# print salary of first employee 
print(employee_data[0,1])


# slicing 
# Python slicing excludes the end index.
# print row number 10 to 20 of employee_data
print(employee_data[10:21])