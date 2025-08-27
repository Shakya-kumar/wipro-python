# ================= Use Case: Outlier Detection =================
# Dataset: datasetExample.csv
#
# Tasks:
# 1. Load the data in the DataFrame
# 2. Detection of Outliers

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("datasetExample.csv")
print("First 5 rows:\n", df.head())

sns.boxplot(data=df)
plt.show()

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

outliers = ((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR)))
print("\nOutliers Detected (True = Outlier):\n", outliers)

