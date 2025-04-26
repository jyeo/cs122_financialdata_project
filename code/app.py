from flask import Flask, render_template, request
from utils.spotify_api import get_spotify_token, get_artist_info, get_top_albums, get_top_tracks
from utils.cache_manager import load_from_cache, save_to_cache
from utils.data_analysis import build_track_dataframe, analyze

app = Flask(__name__)

from utils.visualize import plot_popularity_bar

@app.route("/", methods=["GET", "POST"])
def home():
    artist_info = None
    top_albums = []
    top_tracks = []
    analysis = None
    track_analysis = None
    plot_path = None 

    if request.method == "POST":
        artist_name = request.form.get("artist_name", "").strip()

        # Check if artist_name is in the cache
        if artist_name:
            print("Checking cache for artist:", artist_name, flush=True)
            cached_data = load_from_cache(artist_name)
            if cached_data:
                print("Cache hit for artist:", artist_name)
                artist_info = cached_data.get("artist_info")
                top_albums = cached_data.get("top_albums", [])
                top_tracks = cached_data.get("top_tracks", [])
                
            # If the data is not in the cache, fetch it from Spotify
            else:
                print("Cache miss for artist:", artist_name)
                token = get_spotify_token()
                artist_info = get_artist_info(artist_name, token)

                if artist_info:
                    artist_id = artist_info["id"]
                    top_albums = get_top_albums(artist_id, token)
                    top_tracks = get_top_tracks(artist_id, token)
                    save_to_cache(artist_name, {
                        "artist_info": artist_info,
                        "top_albums": top_albums,
                        "top_tracks": top_tracks
                    })
                else:
                    artist_info = {"error": "Artist not found."}

            # Perform data analysis and visualization if top tracks are available
            if top_tracks:
                df = build_track_dataframe(top_tracks)
                track_analysis = analyze(df)
                plot_popularity_bar(df, artist_name)  # Generate the bar chart
                plot_path = "static/plot.png"  # Path to the generated plot

    return render_template('home.html', artist=artist_info, albums=top_albums, tracks=top_tracks, analysis=analysis, track_analysis=track_analysis, plot_path=plot_path)

if __name__ == "__main__":
    app.run(debug=True)