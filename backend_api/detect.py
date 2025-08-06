from urllib.parse import urlparse

def extract_features(url):
    features = []
    features.append(1 if "@" in url else 0)
    features.append(1 if "-" in url else 0)
    features.append(len(url))
    parsed = urlparse(url)
    features.append(len(parsed.netloc))
    return features