from flask import Flask, request, jsonify
import joblib
import re

app = Flask(__name__)

# Load the trained model and vectorizer
model = joblib.load("phishing_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    url = data.get("url")

    if not url:
        return jsonify({"error": "Missing URL"}), 400

    url_transformed = vectorizer.transform([url])
    prediction = model.predict(url_transformed)[0]

    return jsonify({"prediction": "phishing" if prediction == 1 else "safe"})

@app.route('/')
def home():
    return "PhishGuard AI Model is running!"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
