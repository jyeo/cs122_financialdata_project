from flask import Flask, render_template, request
from utils.spotify_api import get_spotify_token, get_artist_info, get_top_albums

app = Flask(__name__)


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
