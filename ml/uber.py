import builtins as bi
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error

# Load Dataset
df = pd.read_csv("/content/uber.csv")

bi.print("Original Dataset:")
bi.print(df.head())

# 1. Data Preprocessing
df = df.drop(columns=["Unnamed: 0", "key"], errors="ignore")
df = df.dropna()

df["pickup_datetime"] = pd.to_datetime(
    df["pickup_datetime"], errors="coerce"
)
df = df.dropna(subset=["pickup_datetime"])

# Remove invalid values
df = df[
    (df["fare_amount"] > 0) &
    (df["passenger_count"] > 0) &
    (df["pickup_longitude"].between(-180, 180)) &
    (df["dropoff_longitude"].between(-180, 180)) &
    (df["pickup_latitude"].between(-90, 90)) &
    (df["dropoff_latitude"].between(-90, 90))
]

# Extract date and time features
df["hour"] = df["pickup_datetime"].dt.hour
df["day"] = df["pickup_datetime"].dt.day
df["month"] = df["pickup_datetime"].dt.month
df["year"] = df["pickup_datetime"].dt.year

df = df.drop(columns=["pickup_datetime"])

bi.print("\nPreprocessed Dataset:")
bi.print(df.head())

# 2. Identify Outliers using IQR
Q1 = df["fare_amount"].quantile(0.25)
Q3 = df["fare_amount"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[
    (df["fare_amount"] < lower) |
    (df["fare_amount"] > upper)
]

bi.print("\nNumber of Outliers:", bi.len(outliers))

# Remove Outliers
df = df[
    (df["fare_amount"] >= lower) &
    (df["fare_amount"] <= upper)
]

# 3. Correlation
bi.print("\nCorrelation Matrix:")
bi.print(df.corr())

plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# 4. Split Dataset
X = df.drop("fare_amount", axis=1)
y = df["fare_amount"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)

lr_pred = lr.predict(X_test)

# Random Forest Regression
rf = RandomForestRegressor(
    n_estimators=50, random_state=42, n_jobs=-1
)
rf.fit(X_train, y_train)

rf_pred = rf.predict(X_test)

# 5. Model Evaluation
lr_r2 = r2_score(y_test, lr_pred)
lr_rmse = np.sqrt(mean_squared_error(y_test, lr_pred))

rf_r2 = r2_score(y_test, rf_pred)
rf_rmse = np.sqrt(mean_squared_error(y_test, rf_pred))

bi.print("\nLinear Regression Results")
bi.print("R2 Score:", lr_r2)
bi.print("RMSE:", lr_rmse)

bi.print("\nRandom Forest Regression Results")
bi.print("R2 Score:", rf_r2)
bi.print("RMSE:", rf_rmse)

# Model Comparison
results = pd.DataFrame({
    "Model": ["Linear Regression", "Random Forest"],
    "R2 Score": [lr_r2, rf_r2],
    "RMSE": [lr_rmse, rf_rmse]
})

bi.print("\nModel Comparison:")
bi.print(results)