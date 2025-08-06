import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Example data — create simple phishing dataset
data = {
    "length": [20, 80, 15, 100],
    "dots": [1, 5, 0, 6],
    "https": [1, 0, 0, 0],
    "at_symbol": [0, 1, 0, 1],
    "digits": [1, 1, 0, 1],
    "label": [0, 1, 0, 1]  # 0 = safe, 1 = phishing
}

df = pd.DataFrame(data)

X = df.drop("label", axis=1)
y = df["label"]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "phishing_model.pkl")
print("✅ Model saved as phishing_model.pkl")
