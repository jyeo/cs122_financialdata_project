import os
import json

#Load artist data from cache
def load_from_cache(artist_name):
    cache_path = f"data/snapshots/{artist_name.lower().replace(' ', '_')}.json"
    if os.path.exists(cache_path):
        with open(cache_path) as f:
            return json.load(f)
    return None

#Save artist data to cache
def save_to_cache(artist_name, data):
    os.makedirs("data/snapshots", exist_ok=True)
    with open(f"data/snapshots/{artist_name.lower().replace(' ', '_')}.json", "w") as f:
        json.dump(data, f, indent=2)