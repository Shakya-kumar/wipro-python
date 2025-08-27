# ================= Use Case: Data Preprocessing =================
# Dataset: melb_data.csv (Download from Kaggle)
#
# Task: Perform Data Preprocessing on melb_data.csv dataset with statistical perspective using Pandas

import pandas as pd

df = pd.read_csv("melb_data.csv")
print("First 5 rows:\n", df.head())

print("\nStatistical Summary:\n", df.describe(include="all"))

df = df.drop_duplicates()

df = df.dropna(thresh=df.shape[1] - 3)
df = df.fillna(df.mean(numeric_only=True))

categorical_cols = df.select_dtypes(include=['object']).columns
df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

print("\nProcessed DataFrame Shape:", df.shape)
print("\nProcessed DataFrame (first 5 rows):\n", df.head())

