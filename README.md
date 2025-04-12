# CS 122 Project - NEW PROJECT SPOTIFY ANALYSIS

For "TensorFlow and Financial Applications", our team uses SEC EDGAR to collect public financial data and employ TensorFlow to analyse and model financial trends. 

Uilising the SEC EDGAR API and Python, our team collects real-time and financial metrics for specific trends.
(i.e. stock prices, dividends, revenue, and etc.

At the end, our data will be outputted using CSV files.

Financial raw data may employ TensorFlow and/or Pandas Data-reader to organise/sort into visual storytelling.
Please see Project Description for more details.

## Authors

* Aaron Nguyen

* Jasper Yeo

## Project Description (5 sentences)

## Project Outline/Plan
* Interface Plan

The User Interface will allow users to search for an artist and view graphs based on their Spotify data.

Our team’s UI will focus on artist searches and data visualization, with potential for additional features such as track comparisons or genre insights.

Possible other features:

Top tracks over time

Visual comparison of multiple artists

Popularity timeline

* Data Collection and Storage Plan (written by Aaron Nguyen)

For data collection, we will use the Spotify Web API to retrieve artist details, popularity metrics, discography, and top track information.
Data will be retrieved in real time through authorized requests and temporarily stored as JSON or CSV for processing. If needed, directories will be organized by Spotify ID.

* Data Analysis and Visualization Plan (written by Jasper Yeo)
Using financial data retrieved from SEC EDGAR servers (with 0.1 second delays per request), main raw retrieval stream will be categorised into the following: data of revenue, net income, total assets, and total liabilities.
Modified Financial Datasets may be used within the team's user interface for further visual storytelling.

Visual
Pandas Data-reader-related applications may be used to use raw data to be placed into our team's main interface.
Further Visualisation may employ TensorFlow to further apply analysis and improve UX utilisation.

Possible Storytelling may include:
* Top 10 companies based on strengths from total asssets - total liabilities
* Graphs that show annual changes within a 10 year span
* Other stories may be added in lieu of time

## Notes

List of common Git commands
- git pull
- git add *
- git commit -m "message"
- git push

## Extra
A .gitignore file and a license (MIT License) has been attached separately


