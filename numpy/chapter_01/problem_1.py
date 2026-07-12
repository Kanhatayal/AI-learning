# Problem 1: Employee Analytics
# Find:


# Top 10 highest-paid employees
# take 2 columns employee ID or something and salary, sort salary in descending order and take top 10 and store then print

# Employees eligible for promotion
# set certain criteria for this -> if that criteria is fullfilled by that employee then he/she is eligible for promotion

# Employees likely to leave (based on simple rules)
# same as for promotion 

import pandas as pd
import numpy as np
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
print(PROJECT_ROOT)
DATASET_PATH = PROJECT_ROOT / "datasets" / "WA_Fn-UseC_-HR-Employee-Attrition.csv"
print(DATASET_PATH)
df = pd.read_csv(DATASET_PATH)

# Average salary by age group
# take range of age and then  take average of their salary 
# prepare data based on range 

problem_1 = df[["Age","MonthlyIncome"]].to_numpy()

# Age	        Group
# 18 to 25	    Young
# 26 to 35	    Early Career
# 36 to 45	    Mid Career
# 46 to 60	    Senior

young= problem_1[
    (problem_1[:,0] > 18) & 
    (problem_1[:,0] < 25)
]

young_avg_salary  = np.mean(young[:,1])

print("Young avg salary : ", young_avg_salary)

early_career = problem_1[
    (problem_1[:,0] > 26) &
    (problem_1[:,0] < 35)
]

early_career_avg_salary = np.mean(early_career[0:,1])
print("Early avg salary : ", early_career_avg_salary)

mid_career = problem_1[
    (problem_1[:, 0] > 36) &
    (problem_1[:, 0] < 45)
]

mid_career_avg_salary = np.mean(mid_career[0:,1])
print("Mid avg salary : ", mid_career_avg_salary)

senior = problem_1[
    (problem_1[:, 0] > 45) &
    (problem_1[:, 0] < 60)
]

senior_avg_salary = np.mean(senior[:,1])
print("Senior avg salary : ", senior_avg_salary)







