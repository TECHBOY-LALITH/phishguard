import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Sample dataset: Replace this with your real phishing dataset
# CSV should have at least 5 feature columns and a 'label' column
df = pd.read_csv("dataset.csv")  # You can use a dataset from Kaggle

X = df.drop(columns=["label"])
y = df["label"]

model = RandomForestClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, "phishing_model.pkl")
print("Model saved as phishing_model.pkl")
