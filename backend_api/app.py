from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
from utils import extract_features

app = Flask(__name__)
CORS(app)

model = joblib.load("phishing_model.pkl")

@app.route("/check_url", methods=["POST"])
def check_url():
    data = request.get_json()
    url = data.get("url")
    features = extract_features(url)
    prediction = model.predict([features])[0]
    result = "phishing" if prediction == 1 else "safe"
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
