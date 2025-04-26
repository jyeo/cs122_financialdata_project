import pandas as pd
import numpy as np

# Build a DataFrame from the track data
def build_track_dataframe(tracks):
    return pd.DataFrame([{
        "track_name": t["name"],
        "popularity": t["popularity"],
        "album_name": t["album_name"],
        "album_image": t["album_image"],
        "track_url": t["track_url"],
        "preview_url": t["preview_url"]
    } for t in tracks])

#Analyze the DataFrame and return summary statistics
def analyze(df):
    return {
        "average_popularity": np.mean(df["popularity"]),
        "max_popularity": df["popularity"].max(),
        "min_popularity": df["popularity"].min()
    }