import matplotlib
matplotlib.use("Agg")  # Use the Agg backend for non-GUI rendering
import matplotlib.pyplot as plt
import os

def plot_popularity_bar(df, artist_name):
    sorted_df = df.sort_values("popularity", ascending=True)
    plt.figure(figsize=(10, 6))
    plt.barh(sorted_df["track_name"], sorted_df["popularity"], color="skyblue")
    plt.title(f"Track Popularity – {artist_name}")
    plt.xlabel("Popularity")
    plt.xlim(0, 100)
    plt.tight_layout()

    # Create the static folder inside the code directory if it doesn't exist
    static_folder = os.path.join(os.path.dirname(__file__), "../static")
    os.makedirs(static_folder, exist_ok=True)

    # Save the plot in the static folder
    plot_path = os.path.join(static_folder, "plot.png")
    plt.savefig(plot_path)
    plt.close()