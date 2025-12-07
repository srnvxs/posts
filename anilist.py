import requests

API_URL = "https://animmes2uapi.vercel.app/anilist"

def get_anime(query: str):
    try:
        r = requests.get(
            API_URL,
            params={"query": query},
            timeout=15,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        if r.status_code != 200:
            print("HTTP Error:", r.status_code)
            print(r.text)
            return None

        try:
            data = r.json()
        except Exception:
            print("❌ Not JSON Response:")
            print(r.text)
            return None

        if data.get("success") and data.get("anime"):
            return data["anime"]

        return None

    except Exception as e:
        print("Request Failed:", e)
        return None
