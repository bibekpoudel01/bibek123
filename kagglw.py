# Credit Card Fraud Detection using Scikit-learn and Snap ML

# Step 1: Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

from sklearn.linear_model import LogisticRegression
from snapml import LogisticRegression as SnapLogisticRegression

# Step 2: Load the Dataset
df = pd.read_csv("creditcard.csv")

# Step 3: Explore Data
print(df.head())
print(df['Class'].value_counts())

# Step 4: Data Preprocessing
X = df.drop('Class', axis=1)
y = df['Class']

# Normalize 'Amount' column
scaler = StandardScaler()
X['Amount'] = scaler.fit_transform(X[['Amount']])

# Train-test split (with stratification to handle imbalance)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Step 5: Scikit-learn Logistic Regression
print("\n--- Scikit-learn Logistic Regression ---")
start = time.time()
lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, y_train)
sklearn_time = time.time() - start

y_pred_lr = lr.predict(X_test)
y_proba_lr = lr.predict_proba(X_test)[:, 1]

# Evaluation
print(confusion_matrix(y_test, y_pred_lr))
print(classification_report(y_test, y_pred_lr))
print("ROC AUC Score:", roc_auc_score(y_test, y_proba_lr))
print("Training Time: {:.4f} seconds".format(sklearn_time))

# Step 6: Snap ML Logistic Regression
print("\n--- Snap ML Logistic Regression ---")
start = time.time()
snap_lr = SnapLogisticRegression(max_iter=1000, n_jobs=-1)
snap_lr.fit(X_train.values.astype(np.float32), y_train.values.astype(np.float32))
snap_time = time.time() - start

y_pred_snap = snap_lr.predict(X_test.values.astype(np.float32))
y_proba_snap = snap_lr.predict_proba(X_test.values.astype(np.float32))[:, 1]

# Evaluation
print(confusion_matrix(y_test, y_pred_snap))
print(classification_report(y_test, y_pred_snap))
print("ROC AUC Score:", roc_auc_score(y_test, y_proba_snap))
print("Training Time: {:.4f} seconds".format(snap_time))

# Step 7: Visual Comparison
metrics = ['Scikit-learn', 'Snap ML']
times = [sklearn_time, snap_time]

plt.figure(figsize=(6, 4))
plt.bar(metrics, times, color=['blue', 'green'])
plt.title('Training Time Comparison')
plt.ylabel('Time (seconds)')
plt.show()
