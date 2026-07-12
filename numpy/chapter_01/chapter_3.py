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
    "PerformanceRating"
]

employee_data = df[features].to_numpy()

print(employee_data)
print(employee_data.shape)
print(employee_data.ndim)
print(employee_data.size)
print(employee_data.dtype)
print(employee_data.itemsize)
print(employee_data.nbytes)