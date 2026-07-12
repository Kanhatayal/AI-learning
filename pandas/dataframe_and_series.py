import pandas as pd
from pathlib import Path
# import numpy as np
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATASET_PATH = PROJECT_ROOT / "datasets" / "WA_Fn-UseC_-HR-Employee-Attrition.csv"

df = pd.read_csv(DATASET_PATH)


# head() → First rows
# tail() → Last rows
# sample() → Random rows
# print(type(df))
print(df.head())
print(df.head(10))
print(df.tail())
print(df.tail(10))
print(df.sample(10))
print(df.shape)
# (1470, 35) -> 1470 employees and 35 attributes 

print(df.columns)

print(df.dtypes)

print(df.info())