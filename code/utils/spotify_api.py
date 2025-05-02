import requests
import base64

CLIENT_ID = "2ab213b0ce364015aca93253350b4c49"
CLIENT_SECRET = "264a16d2580c46f3ad8f83bba79787dd"

#Get spotify token
def get_spotify_token():
    auth_url = "https://accounts.spotify.com/api/token"
    auth_header = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode("utf-8")
    headers = {
        "Authorization": f"Basic {auth_header}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    response = requests.post(auth_url, headers=headers, data=data)
    response.raise_for_status()
    return response.json()['access_token']

#Get artist info from search
def get_artist_info(artist_name, token):
    search_url = "https://api.spotify.com/v1/search"
    headers = {"Authorization": f"Bearer {token}"}
    params = {"q": artist_name, "type": "artist", "limit": 1}
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    
    data = response.json()
    if data["artists"]["items"]:
        return data["artists"]["items"][0]
    return None

#Get artist top albums from artist id
def get_top_albums(artist_id, token):
    albums_url = f"https://api.spotify.com/v1/artists/{artist_id}/albums"
    albums_params = {
        "limit": 5,
        "offset": 0,
        "include_groups": "album,single,compilation",
        "market": "US"
    }
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(albums_url, headers=headers, params=albums_params)
    response.raise_for_status()
    albums_data = response.json()
    albums = albums_data.get("items", [])

    top_albums = []
    for album in albums:
        name = album.get('name')
        images = album.get('images', [])
        image_url = images[0]['url'] if images else ""
        top_albums.append({'name': name, 'image': image_url})

    return top_albums

#Get album tracks from artist id
def get_top_tracks(artist_id, token, market="US"):
    top_tracks_url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks"
    headers = {"Authorization": f"Bearer {token}"}
    params = {"market": market}
    
    response = requests.get(top_tracks_url, headers=headers, params=params)
    response.raise_for_status()
    tracks_data = response.json()
    
    top_tracks = []
    for track in tracks_data.get("tracks", []):
        top_tracks.append({
            "name": track.get("name"),
            "popularity": track.get("popularity"),
            "preview_url": track.get("preview_url"),
            "album_name": track.get("album", {}).get("name"),
            "album_image": track.get("album", {}).get("images", [{}])[0].get("url", ""),
            "track_url": track.get("external_urls", {}).get("spotify", "")
        })
    top_tracks = sorted(top_tracks, key=lambda x: x["popularity"], reverse=True)
    
    return top_tracks

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
    normalized = [(genre, round((count / max_val) * 100)) for genre, count in sorted_genres]

    return normalized
