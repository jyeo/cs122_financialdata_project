from flask import Flask, render_template, request
import requests
import base64

app = Flask(__name__)

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
    albums_response = requests.get(albums_url, headers=headers, params=albums_params)
    albums_data = albums_response.json()
    albums = albums_data.get("items", [])

    top_albums = []
    for album in albums:
        name = album.get('name')
        images = album.get('images', [])
        image_url = images[0]['url'] if images else ""
        top_albums.append({'name': name, 'image': image_url})

    return top_albums


@app.route("/", methods=["GET", "POST"])
def home():
    artist_info = None
    top_albums = []

    if request.method == "POST":
        artist_name = request.form.get("artist_name", "").strip()

        if artist_name:
            token = get_spotify_token()
            artist_info = get_artist_info(artist_name, token)

            if artist_info:
                artist_id = artist_info["id"]
                top_albums = get_top_albums(artist_id, token)
            else:
                artist_info = {"error": "Artist not found."}

    return render_template('home.html', artist=artist_info, albums=top_albums)

if __name__ == "__main__":
    app.run(debug=True)
