import pandas as pd
import numpy as np

def build_track_dataframe(tracks):
    return pd.DataFrame([{
        "track_name": t["name"],
        "popularity": t["popularity"],
        "duration_ms": t["duration_ms"],
        "album": t["album"]["name"]
    } for t in tracks])

def analyze(df):
    return {
        "average_popularity": np.mean(df["popularity"]),
        "max_popularity": df["popularity"].max(),
        "min_popularity": df["popularity"].min()
    }