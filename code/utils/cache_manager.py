import os
import json

def load_from_cache(artist_name):
    cache_path = f"data/snapshots/{artist_name}.json"
    if os.path.exists(cache_path):
        with open(cache_path) as f:
            return json.load(f)
    return None

def save_to_cache(artist_name, data):
    os.makedirs("data/snapshots", exist_ok=True)
    with open(f"data/snapshots/{artist_name}.json", "w") as f:
        json.dump(data, f, indent=2)