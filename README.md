# 🛡️ PhishGuard – AI-Powered Phishing URL Detector

PhishGuard is a browser extension powered by machine learning that scans URLs in real-time and alerts users if a site is **phishing** or **safe**. It combines a sleek Chrome extension interface with an intelligent Flask-based Python backend that classifies URLs using a trained ML model.

---

## 🌟 Features

- 🔍 Real-time phishing detection
- 🤖 AI-based URL classification (using trained ML model)
- 🔴 Red warning popup for phishing websites
- ✅ Green safe alert for trusted websites
- 🧠 Option to report false positives
- 🌐 Cross-platform usage (Windows / Kali Linux / Termux)
- 🎯 Lightweight and fast

---


---

## ⚙️ Installation Guide

### 🖥️ For Windows / Linux / Termux:

```bash
git clone https://github.com/TECHBOY-LALITH/phishguard
cd phishguard/ai_model
python -m venv venv && source venv/bin/activate  # Windows use: venv\Scripts\activate
pip install -r requirements.txt
python app.py
# Run Flask API
python app.py
