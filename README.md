# CS 122 Project - TensorFlow and Financial Applications

For "TensorFlow and Financial Applications", our team uses SEC EDGAR to collect public financial data and employ TensorFlow to analyse and model financial trends. 

Uilising the SEC EDGAR API and Python, our team collects real-time and financial metrics for specific trends.
(i.e. stock prices, dividends, revenue, and etc.

At the end, our data will be outputted using CSV files.

## Authors

* Aaron Nguyen

* Jasper Yeo

## Project Description (5 sentences)

## Project Outline/Plan
* Interface Plan

The User Interface will allow users to browse standard company financial data.

Due to time restraints, our team's user interface will be limited to browsing, comparison features may be added if time allowance is found.

Other features could include:
* analysis of specific company trends
* financial reports

* Data Collection and Storage Plan (written by Aaron Nguyen)

For data collection, our team will use the SEC EDGAR API to retrieve real-time and historical data.
For storage utilising CSV files, multiple directories organised by each unique ticker symbol. 
CSV files will be devised into annual unique ticker symbol directories.

* Data Analysis and Visualization Plan (written by Jasper Yeo)
Using financial data retrieved from SEC EDGAR servers (with 0.1 second delays per request), main raw retrieval stream will be categorised into the following: data of revenue, net income, total assets, and total liabilities.

Visual
Pandas Data-reader-related applications may be used to use raw data to be placed into our team's main interface.
Further Visualisation may employ TensorFlow to further apply analysis and improve UX utilisation.

## Notes

List of common Git commands
- git pull
- git add *
- git commit -m "message"
- git push

## Extra
A .gitignore file and a license (MIT License) has been attached separately


