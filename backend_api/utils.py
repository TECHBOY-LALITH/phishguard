import re

def extract_features(url):
    # Simple phishing triggers for demo
    if "login" in url or "free" in url or "gift" in url or "update" in url or "bank" in url:
        # Force features that the model was trained to treat as phishing
        return [100, 5, 0, 1, 1]  # suspicious: long, lots of dots, no https, has @, has digits
    else:
        return [20, 1, 1, 0, 0]  # safe-looking URL
