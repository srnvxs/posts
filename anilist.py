import requests

API_URL = "https://animmes2uapi.vercel.app/anilist"

def get_anime(query: str):
    try:
        r = requests.get(API_URL, params={"query": query}, timeout=10)
        r.raise_for_status()
        j = r.json()

        if j.get("success") and j.get("anime"):
            return j["anime"]

        return None
    except Exception as e:
        print(e)
        return None
