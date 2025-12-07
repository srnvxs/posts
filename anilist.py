import requests

API_URL = "https://animmes2uapi.vercel.app/anilist"

def get_anime(name: str):
    try:
        r = requests.get(API_URL, params={"query": name}, timeout=10)
        data = r.json()
        return data.get("data")
    except Exception:
        return None
