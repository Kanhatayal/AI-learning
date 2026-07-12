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

average_salary = np.average(employee_data[:,0])
