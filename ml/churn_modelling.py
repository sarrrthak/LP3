import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. Load Dataset from uploaded file in Google Colab
# Add a forward slash before the filename
df = pd.read_csv("/Churn_Modelling.csv")

print("Original Dataset:")
print(df.head())

# 2. Data Preprocessing
df = df.drop(["RowNumber", "CustomerId", "Surname"], axis=1)

df = df.dropna()

# Encode categorical columns
le = LabelEncoder()

df["Gender"] = le.fit_transform(df["Gender"])
df["Geography"] = le.fit_transform(df["Geography"])

# Separate features and target
X = df.drop("Exited", axis=1)
y = df["Exited"]

# 3. Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 4. Feature Scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 5. Build Neural Network Classifier
# Increased max_iter to 500 to solve the convergence warning
model = MLPClassifier(
    hidden_layer_sizes=(16, 8),
    activation="relu",
    solver="adam",
    max_iter=500,
    random_state=42
)

# Train Model
model.fit(X_train, y_train)

# 6. Make Predictions
y_pred = model.predict(X_test)

# 7. Evaluate Model
print("\nAccuracy:", accuracy_score(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# 8. Predict New Customer
prediction = model.predict(X_test[:1])

if prediction[0] == 1:
    print("\nCustomer will leave the bank.")
else:
    print("\nCustomer will not leave the bank.")