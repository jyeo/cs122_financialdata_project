import matplotlib
matplotlib.use("Agg")  # Use the Agg backend for non-GUI rendering
import matplotlib.pyplot as plt
import os

font_path = "NotoSansSC-Regular.otf"

current_dir = os.path.dirname(__file__)
font_path = os.path.join(current_dir, "../static/fonts/NotoSansSC-Regular.ttf")

from matplotlib import font_manager

font_prop = font_manager.FontProperties(fname=font_path)
plt.rcParams["font.family"] = font_prop.get_name()

matplotlib.rcParams['axes.unicode_minus'] = False


def plot_popularity_bar(df, artist_name):
    sorted_df = df.sort_values("popularity", ascending=True)
    plt.figure(figsize=(10, 6))

    plt.barh(
        sorted_df["track_name"],
        sorted_df["popularity"],
        color="skyblue"
    )

    plt.title(f"Track Popularity – {artist_name}", fontproperties=font_prop, fontsize=16)
    plt.xlabel("Popularity", fontproperties=font_prop, fontsize=14)
    plt.xlim(0, 100)

    ax = plt.gca()
    ax.set_yticklabels(sorted_df["track_name"], fontproperties=font_prop, fontsize=12)

    plt.tight_layout()

    # Create the static folder inside the code directory if it doesn't exist
    static_folder = os.path.join(os.path.dirname(__file__), "../static")
    os.makedirs(static_folder, exist_ok=True)

    # Save the plot in the static folder
    plot_path = os.path.join(static_folder, "plot.png")
    plt.savefig(plot_path)
    plt.close()