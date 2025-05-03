import matplotlib
matplotlib.use("Agg")  # Use the Agg backend for non-GUI rendering
import matplotlib.pyplot as plt
import os
from matplotlib import font_manager

def detect_language(text):
    for char in text:
        if '\u4e00' <= char <= '\u9fff':
            return 'chinese'
        if '\u3040' <= char <= '\u309f' or '\u30a0' <= char <= '\u30ff':
            return 'japanese'
        if '\uac00' <= char <= '\ud7af':
            return 'korean'
    return 'general'

def load_font(language='general'):
    current_dir = os.path.dirname(__file__)
    if language == 'chinese':
        font_file = "../static/fonts/NotoSansSC-Regular.ttf"
    elif language == 'japanese':
        font_file = "../static/fonts/NotoSansJP-Regular.ttf"
    elif language == 'korean':
        font_file = "../static/fonts/NotoSansKR-Regular.ttf"
    else:
        font_file = "../static/fonts/NotoSans-Regular.ttf"

    font_path = os.path.join(current_dir, font_file)

    if not os.path.exists(font_path):
        print(f" Warning: Font not found at {font_path}. Using default font.")
        return None

    font_prop = font_manager.FontProperties(fname=font_path)
    plt.rcParams["font.family"] = font_prop.get_name()
    plt.rcParams['axes.unicode_minus'] = False
    return font_prop

def plot_popularity_bar(df, artist_name, font_choice='general'):

    artist_name = artist_name.title()
    font_prop = load_font(font_choice)

    sorted_df = df.sort_values("popularity", ascending=True)
    plt.figure(figsize=(10, 6))

    plt.barh(
        sorted_df["track_name"],
        sorted_df["popularity"],
        color="#206fb2"
    )
    if font_prop:
        plt.title(f"Track Popularity – {artist_name}", fontproperties=font_prop, fontsize=16)
        plt.xlabel("Popularity", fontproperties=font_prop, fontsize=14)
    else:
        plt.title(f"Track Popularity – {artist_name}", fontsize=16)
        plt.xlabel("Popularity", fontsize=14)

    plt.xlim(0, 100)

    ax = plt.gca()
    if font_prop:
        ax.set_yticklabels(sorted_df["track_name"], fontproperties=font_prop, fontsize=12)
    else:
        ax.set_yticklabels(sorted_df["track_name"], fontsize=12)

    plt.tight_layout()

    static_folder = os.path.join(os.path.dirname(__file__), "../static")
    os.makedirs(static_folder, exist_ok=True)

    plot_path = os.path.join(static_folder, "plot.png")
    plt.savefig(plot_path)
    plt.close()

def plot_genre_popularity_bar(genre_data, year):
    genres = [g[0] for g in genre_data]
    popularity = [g[1] for g in genre_data]

    plt.figure(figsize=(10, 6))
    plt.barh(genres[::-1], popularity[::-1], color="teal")
    plt.title(f"Top Genres of {year}", fontsize=16)
    plt.xlabel("Popularity (0–100)", fontsize=12)
    plt.tight_layout()
    plt.xlim(0, 100)

    static_folder = os.path.join(os.path.dirname(__file__), "../static")
    os.makedirs(static_folder, exist_ok=True)
    plot_path = os.path.join(static_folder, f"genre_plot_{year}.png")
    plt.savefig(plot_path)
    plt.close()

    return f"static/genre_plot_{year}.png"

def plot_genre_artist_bar(artist_data, genre_name):
    names = [a[0] for a in artist_data]
    popularity = [a[1] for a in artist_data]

    plt.figure(figsize=(10, 6))
    plt.barh(names[::-1], popularity[::-1], color="#9933ff")
    plt.title(f"Top Artists – {genre_name.title()}", fontsize=16)
    plt.xlabel("Popularity", fontsize=12)
    plt.tight_layout()
    plt.xlim(0, 100)

    static_folder = os.path.join(os.path.dirname(__file__), "../static")
    os.makedirs(static_folder, exist_ok=True)
    plot_path = os.path.join(static_folder, f"top_artists_{genre_name}.png")
    plt.savefig(plot_path)
    plt.close()

    return f"static/top_artists_{genre_name}.png"
