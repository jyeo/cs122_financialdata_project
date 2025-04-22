import matplotlib.pyplot as plt
import os

def plot_popularity_bar(df, artist_name):
    sorted_df = df.sort_values("popularity", ascending=True)
    plt.figure(figsize=(10, 6))
    plt.barh(sorted_df["track_name"], sorted_df["popularity"])
    plt.title(f"Track Popularity – {artist_name}")
    plt.xlabel("Popularity")
    plt.tight_layout()
    os.makedirs("static", exist_ok=True)
    plt.savefig("static/plot.png")
    plt.close()