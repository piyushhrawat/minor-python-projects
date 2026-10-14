import requests
from urllib.parse import urlparse

API_KEY = "YOUR_GOOGLE_SAFE_BROWSING_API_KEY"

# Trusted domains (you can expand this list)
trusted_domains = ["riotgames.com", "paypal.com", "amazon.com"]

def check_with_google_safe_browsing(url):
    endpoint = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={API_KEY}"
    payload = {
        "client": {"clientId": "link-checker", "clientVersion": "1.0"},
        "threatInfo": {
            "threatTypes": [
                "MALWARE",
                "SOCIAL_ENGINEERING",
                "UNWANTED_SOFTWARE",
                "POTENTIALLY_HARMFUL_APPLICATION"
            ],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]
        }
    }
    response = requests.post(endpoint, json=payload)
    return bool(response.json().get("matches"))

def is_trusted_domain(url):
    domain = urlparse(url).netloc.lower()
    return any(td in domain for td in trusted_domains)

def looks_like_typosquatting(url):
    suspicious_patterns = ["ri0t", "paypa1", "faceb00k", "g00gle"]
    return any(sp in url.lower() for sp in suspicious_patterns)

def check_link(url):
    if check_with_google_safe_browsing(url):
        return f"❌ {url} is unsafe (phishing/malware detected by Google Safe Browsing)."
    elif is_trusted_domain(url):
        return f"✅ {url} is safe (trusted domain)."
    elif looks_like_typosquatting(url):
        return f"⚠️ {url} looks suspicious (possible typosquatting)."
    else:
        return f"❓ {url} not flagged, but be cautious."

# Example usage
urls = [
]

for u in urls:
    print(check_link(u))
