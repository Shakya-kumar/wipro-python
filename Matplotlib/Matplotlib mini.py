# ================= Use Case: Diabetes Prediction =================
# Dataset: Diabetes.csv (Download from Kaggle)
#
# Tasks:
# 1. Load the data in the DataFrame
# 2. Data Pre-processing
# 3. Handle the Categorical Data
# 4. Perform Uni-variate Analysis
# 5. Perform Bi-variate Analysis

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Diabetes.csv")
print("First 5 rows:\n", df.head())

df = df.drop_duplicates()
df = df.fillna(df.mean(numeric_only=True))

categorical_cols = df.select_dtypes(include=['object']).columns
df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

print("\nStatistical Summary:\n", df.describe())

for col in df.columns:
    plt.figure(figsize=(6,4))
    sns.histplot(df[col], kde=True)
    plt.title(f"Univariate Analysis of {col}")
    plt.show()

plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Bivariate Analysis - Correlation Heatmap")
plt.show()

sns.pairplot(df)
plt.show()

