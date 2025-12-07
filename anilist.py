import requests

API_URL = "https://anilist.vercel.app/api/graphql"

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

        data = r.json()

        if data.get("success") and data.get("anime"):
            return data["anime"]

        return None

    except Exception as e:
        print("Request Failed:", e)
        return None
