import requests

API_URL = "https://graphql.anilist.co"

def get_anime(name: str):
    query = """
    query ($search: String) {
      Media(search: $search, type: ANIME) {
        title {
          romaji
        }
        description
      }
    }
    """

    variables = {
        "search": name
    }

    try:
        r = requests.post(
            API_URL,
            json={
                "query": query,
                "variables": variables
            },
            headers={
                "User-Agent": "Mozilla/5.0",
                "Content-Type": "application/json"
            },
            timeout=15
        )

        if r.status_code != 200:
            print("HTTP Error:", r.status_code)
            print(r.text)
            return None

        data = r.json()

        media = data.get("data", {}).get("Media")
        if not media:
            return None

        return {
            "title": media["title"]["romaji"],
            "description": media["description"] or "Synopsis not available."
        }

    except Exception as e:
        print("Request Failed:", e)
        return None
