import pandas as pd
import numpy as np
from pathlib import Path
import time 

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


# 4.1 Boolean Masking


# Employees older than 40
print(employee_data[employee_data[:,0] > 40])

# Salary greater than 10000
print(employee_data[employee_data[:,1] > 10000])

# Employees with more than 10 years at company
print(employee_data[employee_data[:,2] > 10])

# Employees with more than 10 years at company
print(employee_data[(employee_data[:,0] < 40) & (employee_data[:,0] > 30)])

# Employees with salary > 10000 and performance rating = 4.
print(employee_data[(employee_data[:,1] > 10000) & (employee_data[:,3] > 4)])

# 4.2 Fancy Indexing

# Select employee 0, 10 and 25
print(employee_data[[0,10,25]])

# Select Age and PerformanceRating
print(employee_data[:, [0, 3]])
print(employee_data[:10,[0,3]])

print(employee_data[[5,50,100,500]])

print(employee_data[0:,[0,1]])


# 4.3 Vectorized Operations

employee_data[:,0] += 10
print(employee_data[:,0])

# Why?

# NumPy executes these operations in optimized C code, 
# avoiding explicit Python loops.

# 4.4 Broadcasting

# NumPy automatically expands arrays of compatible shapes during operations.

print(employee_data[[1,2,3,4]])
bonus = np.array([10000,50000,1000,1000])
updated_salary = employee_data[:, :4] + bonus
print(updated_salary)

# mean salary 
print(np.mean(employee_data[:,1]))
print(np.max(employee_data[:,1]))
print(np.min(employee_data[:,1]))
print(np.std(employee_data[:,1]))
print(np.sum(employee_data[:, 1]))

# rowwise operation 
print(np.mean(employee_data, axis = 1))

# column wise operation 
print(np.mean(employee_data, axis = 0))

# 4.6 Reshaping

salary = employee_data[:, 1]
print(salary.shape)
# [5993, 5130, 2090, 2909, 3468, ...]

salary = salary.reshape(-1,1)

print(salary.shape)
# [
#  [5993],
#  [5130],
#  [2090],
#  [2909],
#  [3468],
#  ...
# ]

# 4.7 Views vs Copies

# A view shares memory with the original array.

# A copy allocates new memory.

view = employee_data[:, :2]
view[0,0] = 999
print(employee_data[0])
# [ 999 5993    6    3    1   11]

copy = employee_data[:, :2].copy()

copy[0,0] = 0
print(employee_data[0])
# unchanged data
# [ 999 5993    6    3    1   11]

# 4.8 Memory Layout

print(employee_data.flags)
# C_CONTIGUOUS : False this is false means data is not contigously allocated in memory
#   F_CONTIGUOUS : True
#   OWNDATA : False
#   WRITEABLE : True
#   ALIGNED : True
#   WRITEBACKIFCOPY : False

# 4.9 Performance Benchmarking

numbers = np.arange(1_000_000)
start = time.perf_counter()
result = numbers*2
print(time.perf_counter() - start)