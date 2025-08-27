# Q1. Create a model that can predict the disease of cancer based on features given in the dataset. Use appropriate evaluation metrics. Dataset cancer.csv Logistic Regression and Evaluation Metrics
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data = pd.read_csv("cancer.csv")
X = data.drop("target", axis=1)
y = data["target"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Cancer Dataset Results")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))


# Q2. Create a model that can predict that the customer has purchased item or not based on features given in the dataset. Use appropriate evaluation metrics. Dataset Social_Network_Ads.csv Logistic Regression and Evaluation Metrics
data2 = pd.read_csv("Social_Network_Ads.csv")
X = data2.iloc[:, :-1].values
y = data2.iloc[:, -1].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
model2 = LogisticRegression(max_iter=1000)
model2.fit(X_train, y_train)
y_pred2 = model2.predict(X_test)
print("Social Network Ads Dataset Results")
print("Accuracy:", accuracy_score(y_test, y_pred2))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred2))
print("Classification Report:\n", classification_report(y_test, y_pred2))
