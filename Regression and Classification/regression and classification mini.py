# ================= Use Case 1: Diabetes Prediction =================
# Dataset: PIMA Indians Diabetes Dataset (Download from Kaggle)
#
# Tasks:
# 1. Load the data in the DataFrame
# 2. Perform Data Preprocessing
# 3. Perform Exploratory Data Analysis
# 4. Build the model using Logistic Regression and K-Nearest Neighbour
# 5. Use the appropriate evaluation metrics

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

df = pd.read_csv("diabetes.csv")
print("First 5 rows:\n", df.head())

df = df.drop_duplicates()
df = df.fillna(df.mean(numeric_only=True))

print("\nStatistical Summary:\n", df.describe())

sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

X = df.drop("Outcome", axis=1)
y = df["Outcome"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

log_model = LogisticRegression()
log_model.fit(X_train, y_train)
y_pred_log = log_model.predict(X_test)

print("\nLogistic Regression Accuracy:", accuracy_score(y_test, y_pred_log))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_log))
print("Classification Report:\n", classification_report(y_test, y_pred_log))

knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train, y_train)
y_pred_knn = knn_model.predict(X_test)

print("\nKNN Accuracy:", accuracy_score(y_test, y_pred_knn))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_knn))
print("Classification Report:\n", classification_report(y_test, y_pred_knn))



# ================= Use Case 2: Sales Prediction =================
# Dataset: Advertising.csv (Download from Kaggle)
#
# Tasks:
# 1. Load the data in the DataFrame
# 2. Perform Data Preprocessing
# 3. Handle Categorical Data
# 4. Perform Exploratory Data Analysis
# 5. Build the model using Multiple Linear Regression
# 6. Use the appropriate evaluation metrics

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

sales = pd.read_csv("Advertising.csv")
print("First 5 rows:\n", sales.head())

sales = sales.drop_duplicates()
sales = sales.fillna(sales.mean(numeric_only=True))

categorical_cols = sales.select_dtypes(include=['object']).columns
sales = pd.get_dummies(sales, columns=categorical_cols, drop_first=True)

print("\nStatistical Summary:\n", sales.describe())

sns.pairplot(sales)
plt.show()

X = sales.drop("Sales", axis=1)
y = sales["Sales"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

lin_model = LinearRegression()
lin_model.fit(X_train, y_train)
y_pred = lin_model.predict(X_test)

print("\nMultiple Linear Regression RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("R2 Score:", r2_score(y_test, y_pred))
