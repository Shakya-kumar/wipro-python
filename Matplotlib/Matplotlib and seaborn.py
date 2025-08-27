# ================= Use Case 1: Mall Customers =================
# Dataset: Mall_Customers.csv (Download from Kaggle)
#
# Task: Perform Exploratory Data Analysis using Matplotlib and Seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

mall = pd.read_csv("Mall_Customers.csv")
print("First 5 rows:\n", mall.head())

print("\nStatistical Summary:\n", mall.describe(include="all"))

plt.figure(figsize=(6,4))
sns.histplot(mall['Age'], bins=20, kde=True)
plt.title("Age Distribution")
plt.show()

plt.figure(figsize=(6,4))
sns.countplot(x='Gender', data=mall)
plt.title("Gender Count")
plt.show()

plt.figure(figsize=(6,4))
sns.scatterplot(x='Age', y='Spending Score (1-100)', hue='Gender', data=mall)
plt.title("Age vs Spending Score")
plt.show()

sns.pairplot(mall)
plt.show()



# ================= Use Case 2: Salary Data =================
# Dataset: Salary_data.csv (Download from Kaggle)
#
# Task: Perform Exploratory Data Analysis using Matplotlib and Seaborn

salary = pd.read_csv("Salary_data.csv")
print("\nFirst 5 rows:\n", salary.head())

print("\nStatistical Summary:\n", salary.describe())

plt.figure(figsize=(6,4))
sns.histplot(salary['YearsExperience'], bins=10, kde=True)
plt.title("Years of Experience Distribution")
plt.show()

plt.figure(figsize=(6,4))
sns.histplot(salary['Salary'], bins=10, kde=True)
plt.title("Salary Distribution")
plt.show()

plt.figure(figsize=(6,4))
sns.scatterplot(x='YearsExperience', y='Salary', data=salary)
plt.title("Years of Experience vs Salary")
plt.show()

sns.heatmap(salary.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()



# ================= Use Case 3: Social Network Ads =================
# Dataset: Social_Network_Ads.csv (Download from Kaggle)
#
# Task: Perform Exploratory Data Analysis using Matplotlib and Seaborn

social = pd.read_csv("Social_Network_Ads.csv")
print("\nFirst 5 rows:\n", social.head())

print("\nStatistical Summary:\n", social.describe(include="all"))

plt.figure(figsize=(6,4))
sns.countplot(x='Gender', data=social)
plt.title("Gender Count")
plt.show()

plt.figure(figsize=(6,4))
sns.histplot(social['Age'], bins=15, kde=True)
plt.title("Age Distribution")
plt.show()

plt.figure(figsize=(6,4))
sns.histplot(social['EstimatedSalary'], bins=15, kde=True)
plt.title("Salary Distribution")
plt.show()

plt.figure(figsize=(6,4))
sns.scatterplot(x='Age', y='EstimatedSalary', hue='Purchased', data=social)
plt.title("Age vs Estimated Salary by Purchase Decision")
plt.show()

sns.heatmap(social.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
