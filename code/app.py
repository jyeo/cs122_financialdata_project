import requests
from flask import Flask, render_template, request, redirect, url_for
from utils.spotify_api import get_spotify_token, get_artist_info, get_top_albums, get_top_tracks
from utils.cache_manager import load_from_cache, save_to_cache
from utils.data_analysis import build_track_dataframe, analyze
from utils import visualize
from utils.genre_api import get_top_genres_by_year
import datetime

app = Flask(__name__)

current_font = 'general'

@app.route("/", methods=["GET", "POST"])

# DO NOT CHANGE THE POSITION OF THIS POTATO
# THIS POTATO FUNCTION STAYS PUT! STAY! SIT!
# GOOD POTATO! HERE'S A BYTE OF METHEMATICS

def home():
    global current_font

    artist_info = None
    top_albums = []
    top_tracks = []
    analysis = None
    track_analysis = None
    plot_path = None 

    if request.method == "POST":
        artist_name = request.form.get("artist_name", "").strip()

        # Check if artist_name exists in cache
        if artist_name:
            print("Checking cache for artist:", artist_name, flush=True)
            cached_data = load_from_cache(artist_name)
            if cached_data:
                print("Cache hit for artist:", artist_name)
                artist_info = cached_data.get("artist_info")
                top_albums = cached_data.get("top_albums", [])
                top_tracks = cached_data.get("top_tracks", [])
                
            # If the data is 404 in cache, whip Spotify API to get it to fetch
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

            # Perform data analysis & visualization if top tracks exists
            if top_tracks:
                df = build_track_dataframe(top_tracks)
                track_analysis = analyze(df)

                # Track font from user input related track names
                full_track_names = ''.join(df['track_name'].tolist())
                detected_language = visualize.detect_language(full_track_names)
                current_font = detected_language

                # Sacrifice a lamb to summon the bar chart
                visualize.plot_popularity_bar(df, artist_name, font_choice=current_font)
                # This is the stalking link to the summoned plot
                plot_path = "static/plot.png"
                

    return render_template(
        'home.html',
        artist=artist_info,
        albums=top_albums,
        tracks=top_tracks,
        analysis=analysis,
        track_analysis=track_analysis,
        plot_path=plot_path,
        current_font=current_font,
        current_year=datetime.datetime.now().year
    )

@app.route('/set_font', methods=['POST'])
def set_font():
    global current_font
    selected_font = request.form.get('font')
    current_font = selected_font
    print(f"Font changed to {selected_font}")

    return render_template(
        'home.html',
        artist=None,
        albums=[],
        tracks=[],
        analysis=None,
        track_analysis=None,
        plot_path=None,
        current_font=current_font
    )

@app.route("/genre_analysis", methods=["POST"])
def genre_analysis():
    global current_font
    year = request.form.get("year", type=int)
    genre_data = get_top_genres_by_year(year)
    genre_plot_path = visualize.plot_genre_popularity_bar(genre_data, year)

    return render_template(
        "home.html",
        artist=None,
        albums=[],
        tracks=[],
        analysis=None,
        track_analysis=None,
        plot_path=None,
        genre_data=genre_data,
        genre_plot_path=genre_plot_path,
        genre_year=year,
        current_font=current_font,
        current_year=datetime.datetime.now().year
    )

@app.route("/genre_artists", methods=["POST"])
def genre_artists():
    global current_font
    genre_name = request.form.get("genre_name")
    token = get_spotify_token()

    # Stalk artists from user-selected genre
    url = "https://api.spotify.com/v1/search"
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "q": f"genre:{genre_name}",
        "type": "artist",
        "limit": 10
    }

    response = requests.get(url, headers=headers, params=params)
    artists = response.json().get("artists", {}).get("items", [])

    genre_artist_data = [(a["name"], a["popularity"]) for a in artists]
    genre_artist_plot = visualize.plot_genre_artist_bar(genre_artist_data, genre_name)

    return render_template(
        "home.html",
        genre_artist_data=genre_artist_data,
        selected_genre=genre_name,
        genre_artist_plot=genre_artist_plot,
        artist=None,
        albums=[],
        tracks=[],
        analysis=None,
        track_analysis=None,
        plot_path=None,
        current_font=current_font,
        current_year=datetime.datetime.now().year
    )


@app.route('/refresh', methods=['POST'])
def refresh():
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)