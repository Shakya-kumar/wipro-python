# ================= Use Case: House Price Prediction =================
# Dataset: melb_data.csv (Download from Kaggle)
#
# Tasks:
# 1. Load the data in dataframe (Pandas)
# 2. Handle inappropriate data
# 3. Handle the missing data
# 4. Handle the categorical data

import pandas as pd

df = pd.read_csv("melb_data.csv")
print("First 5 rows:\n", df.head())

df = df.drop_duplicates()

df = df.dropna(thresh=df.shape[1] - 3)
df = df.fillna(df.mean(numeric_only=True))

categorical_cols = df.select_dtypes(include=['object']).columns
df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

print("\nProcessed DataFrame Shape:", df.shape)
print("\nProcessed DataFrame (first 5 rows):\n", df.head())
