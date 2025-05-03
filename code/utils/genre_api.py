import requests
from utils.spotify_api import get_spotify_token

def get_top_genres_by_year(year, token=None, limit=50):
    if token is None:
        token = get_spotify_token()

    headers = {"Authorization": f"Bearer {token}"}
    genres_count = {}

    query = f"year:{year}"
    search_url = "https://api.spotify.com/v1/search"
    params = {
        "q": query,
        "type": "track",
        "limit": limit
    }

    response = requests.get(search_url, headers=headers, params=params)
    results = response.json()
    tracks = results.get("tracks", {}).get("items", [])

    artist_ids = list({artist['id'] for track in tracks for artist in track['artists']})

    for artist_id in artist_ids:
        artist_url = f"https://api.spotify.com/v1/artists/{artist_id}"
        res = requests.get(artist_url, headers=headers)
        if res.status_code == 200:
            data = res.json()
            for genre in data.get("genres", []):
                genres_count[genre] = genres_count.get(genre, 0) + 1

    sorted_genres = sorted(genres_count.items(), key=lambda x: x[1], reverse=True)[:10]
    max_val = sorted_genres[0][1] if sorted_genres else 1
    normalized = [(genre.title(), round((count / max_val) * 100)) for genre, count in sorted_genres]

    return normalized