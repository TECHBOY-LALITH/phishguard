import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load CSV dataset
df = pd.read_csv("../data/phishing_dataset.csv")

# Clean URLs (remove http/https for consistency)
df['url'] = df['url'].str.replace(r"https?://", "", regex=True)

# Features and Labels
X = df['url']
y = df['label']

# Convert URLs to numeric features
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Split (optional for testing)
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save trained model
with open("phishing_model.pkl", "wb") as f:
    pickle.dump(model, f)

# Save vectorizer
with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Model and vectorizer saved successfully in ai_model/")
