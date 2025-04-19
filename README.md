# CS 122 Project - SPOTIFY ANALYSIS: Browsing through

## Authors

* Aaron Nguyen

* Jasper Yeo

## Project Description (5 sentences)

Our team is creating a Spotify application that gives users new retrospectives.
Our user interface will enable users access to our app's backend that captures snapshots of data for local storage.
The pipelines follow the generic format of sending a request to Spotify's API to retrieve a snapshot of data into a cache ,,, or a CSV.
From the data containers, analysis that enables storytelling that includes: top tracks over preset time intervals, comparison of multiple artists, bar chart on a song track's volatility, and etc...
The storage of data analysis into graphical approaches like pandas and etc... will be given to the user via our app.


## Project Outline/Plan

Interface Plan

The User Interface will allow users to search for an artist and view graphs based on Spotify data.

Our team’s UI will focus on artist searches and data visualization, with potential for additional features such as track comparisons or genre insights.

Possible other features:

* Top tracks over time

* Visual comparison of multiple artists

* Popularity timeline

## Data Collection and Storage Plan (written by Aaron Nguyen)

For data collection, we will use the Spotify Web API to retrieve data details artist details, popularity metrics, discography, and top track information.

Data will be retrieved in real time or through a cache through authorised requests and temporarily stored as JSON or CSV for processing. 
ALternatively, the design may be changed to store data with CSV or a cache - depending on overhead costs.
If needed, directories will be organized by Spotify ID.


## Data Analysis and Visualization Plan (written by Jasper Yeo)


Visual
Pandas Data-reader-related applications may be used to use raw data to be placed into our team's main interface.

Main features of UI will guide the storytelling powered by the snapshot data retrieved from a cache.


## Notes

List of common Git commands
- git pull
- git add *
- git commit -m "message"
- git push

## Extra
A .gitignore file and a license (MIT License) has been attached separately


