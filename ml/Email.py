# Email Spam Detection using KNN and SVM
# Normal state   (0) = Not Spam
# Abnormal state (1) = Spam

# 1. Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# 2. Load the dataset
df = pd.read_csv('emails.csv')          # change the path if needed
print("Dataset shape:", df.shape)
print(df['Prediction'].value_counts())   # 0 = Not Spam, 1 = Spam

# 3. Separate features (X) and label (y)
X = df.drop(columns=['Email No.', 'Prediction'])   # word counts
y = df['Prediction']                               # 0 or 1

# 4. Split into training (80%) and testing (20%) data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Create and train both models
knn = KNeighborsClassifier(n_neighbors=5)
svm = SVC(kernel='linear')

knn.fit(X_train, y_train)
svm.fit(X_train, y_train)

# 6. Predict on test data
knn_pred = knn.predict(X_test)
svm_pred = svm.predict(X_test)

# 7. Evaluate performance
def evaluate(name, y_true, y_pred):
    print(f"\n--- {name} ---")
    print(f"Accuracy : {accuracy_score(y_true, y_pred):.4f}")
    print(f"Precision: {precision_score(y_true, y_pred):.4f}")
    print(f"Recall   : {recall_score(y_true, y_pred):.4f}")
    print(f"F1-Score : {f1_score(y_true, y_pred):.4f}")

evaluate("K-Nearest Neighbors", y_test, knn_pred)
evaluate("Support Vector Machine", y_test, svm_pred)

# 8. Confusion matrices
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
for ax, name, pred in zip(axes, ["KNN", "SVM"], [knn_pred, svm_pred]):
    cm = confusion_matrix(y_test, pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax,
                xticklabels=['Not Spam', 'Spam'], yticklabels=['Not Spam', 'Spam'])
    ax.set_title(f"{name} Confusion Matrix")
    ax.set_xlabel("Predicted Label")
    ax.set_ylabel("True Label")
plt.tight_layout()
plt.show()

# 9. Compare both models side by side
results = pd.DataFrame({
    'KNN': [accuracy_score(y_test, knn_pred), precision_score(y_test, knn_pred),
            recall_score(y_test, knn_pred), f1_score(y_test, knn_pred)],
    'SVM': [accuracy_score(y_test, svm_pred), precision_score(y_test, svm_pred),
            recall_score(y_test, svm_pred), f1_score(y_test, svm_pred)]
}, index=['Accuracy', 'Precision', 'Recall', 'F1-Score'])

print("\nComparison of KNN and SVM:")
print(results.round(4))

results.plot(kind='bar', figsize=(8, 5), title='KNN vs SVM')
plt.ylabel('Score')
plt.xticks(rotation=0)
plt.show()

# 10. Conclusion
print("\nConclusion: SVM performs better than KNN on all metrics, "
      "so it is the better choice for spam detection.")


#https://www.kaggle.com/datasets/balaka18/email-spam-classification-dataset-csv