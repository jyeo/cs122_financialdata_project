# 🎶 CS 122 Project – Graphify: Visual Storytelling with Spotify Data

## 👥 Authors

* Aaron Nguyen

* Jasper Yeo

## Requirements
flask
matplotlib
numpy
pandas
requests

Group install using `conda`

```python
sudo conda install flask matplotlib numpy pandas requests
```

Group install using `pip`

```python
sudo pip install flask matplotlib numpy pandas requests
```

## Project Description (5 sentences)

Graphify is a Spotify-powered web application that transforms raw artist data into compelling visual stories. 
Through an intuitive user interface, users can search for their favorite artists and instantly view engaging visualizations based on Spotify’s metrics
(e.g. like popularity trends, discographies, and track comparisons).
The U.I. will also enable users access to our app's backend that captures snapshots of data for local storage.

All in real time or from stored data, our backend interacts with the Spotify Web API; retrieves artist snapshots; and caches them locally (JSON or CSV), which are then processed for storytelling. 

These stories are presented visually using tools like Pandas, Matplotlib, and custom charting techniques

From the data containers, analysis that enables storytelling that includes: top tracks over preset time intervals, comparison of multiple artists, bar chart on a song track's volatility, and etc...

The storage of data analysis into graphical approaches like pandas and etc... will be given to the user via our app.


## Project Outline/Plan

Interface Plan

The User Interface will allow users to search for an artist and view graphs based on Spotify data.

Our team’s UI will focus on artist searches and data visualization, with potential for additional features such as track comparisons or genre insights.

Other Proposed features:

* Top tracks over time

* Visual comparison of multiple artists

* Popularity timeline

What Made the Cut:

* Search for any artist by name

* View top tracks over fixed time intervals

* Compare popularity trends across multiple artists

* Explore track volatility and other interesting metrics

* Potential for future genre-level or playlist-level analysis


## 🗂 Data Collection and Storage Plan (written by Aaron Nguyen)

For data collection, we will use the Spotify Web API to retrieve data details artist details, popularity metrics, discography, and top track information.

Data will be retrieved in real time or through a cache through authorised requests and temporarily stored as JSON or CSV for processing. 
ALternatively, the design may be changed to store data with CSV or a cache - depending on overhead costs.
If needed, directories will be organized by Spotify ID.

📌 Executive Summary:

* Uses the Spotify Web API for real-time artist metadata, discography, and popularity scores
* Organized using Spotify Artist IDs
* Data is either:
  * Cached via local JSON files (for speed + rate limits)
  * Stored in CSV format (for persistence and analysis)

## 📊 Data Analysis and Visualization Plan (written by Jasper Yeo)

Pandas Data-reader-related applications may be used to use raw data to be placed into our team's main interface.
Main features of UI will guide the storytelling powered by the snapshot data retrieved from a cache.

📌 Executive Summary:

* Built-in analysis using Pandas

* Snapshot-style data parsing and structuring for visual output

* Chart types include:
  * Bar charts for track performance
  * Line plots for popularity over time
  * Custom artist comparison graphs
 
## 🛠 Tech Stack
| Layer         | Tools Used                       |
| ------------- | -------------------------------- |
| **Frontend**  | HTML + CSS (via Flask templates) |
| **Backend**   | Python + Flask                   |
| **Data**      | Spotify Web API, JSON, CSV       |
| **Libraries** | Pandas, Matplotlib, Requests     |

## How to Start 101

1. Do some inhumane cloning

```python
git clone https://github.com/your-username/graphify.git
cd graphify/code
```

2. Set up the environment

```python
python -m venv testbox
source testbox/bin/activate  # On Windows: testbox\Scripts\activate
pip install -r requirements.txt
```

3. Configure Spotify API credentials

* Register at [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
* Add your `client_id` and `client_secret` in `utils/spotify_api.py` or store them in an `.env` file

4. Run our team's application 

```python
cd to our main folder containing app.py or use your favourite IDE
python app.py
```

Then open your browser at `http://localhost:5000` or other open port.

## 📁 Folder Structure
```
code/
├── app.py                  # Main Flask app
├── templates/              # HTML templates for UI
├── static/                 # CSS and assets
├── utils/                  # Modular backend components
│   ├── spotify_api.py
│   ├── data_analysis.py
│   ├── visualize.py
│   └── cache_manager.py
└── data/                   # Cached Spotify data (JSON or CSV)
```

## Notes

List of common Git commands
- git pull
- git add *
- git commit -m "message"
- git push

Caching ensures Spotify rate limits aren’t exceeded during development

## Extra
A .gitignore file and a license (MIT License) has been attached separately


