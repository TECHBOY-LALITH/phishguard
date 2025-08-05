import re

def extract_features(url):
    return [
        len(url),
        url.count('.'),
        int(bool(re.search(r'https', url))),
        int(bool(re.search(r'@', url))),
        int(bool(re.search(r'\d', url))),
    ]
