# assignment_1
This repository contains 2 files of .ipynb and .py files, where the former one contains data from IMDB website of movies 2024 list scrapped using selenium and the latter contains application build up using Streamlit containing data visualization and filtering options

# Project Overview - IMDb Movie Scraper
This project is an IMDb movie scraper that automates the process of extracting movie details such as Title, Duration, Rating, Votes, and Genre for movies released in 2024. The extracted data is stored in CSV files for further analysis.

The script uses Selenium to navigate the IMDb website, interact with dropdowns, click buttons, and retrieve structured data dynamically loaded on the webpage.

Features
Scrapes IMDb for movie titles, durations, ratings, votes, and genres.
Handles dynamic content loading by clicking the "Load More" button.
Saves the scraped data into structured CSV files.
Automates navigation and interaction using Selenium WebDriver.

Technologies Used
Python (for scripting and automation)
Selenium WebDriver (for browser automation and web scraping)
CSV (for structured data storage)
Regular Expressions (re) (for text extraction and cleanup)

Steps Involved
Install Python and required libraries (eg: pip install selenium).
Ensure ChromeDriver is installed and matches your Chrome version.
Run the Script
Execute the Python script to scrape movie data from IMDb.
The script navigates the IMDb site, selects genres, and extracts data.
Save Data
Extracted movie details are saved in CSV files categorized by genre.

Future Enhancements
Store data in a database instead of CSV.
Implement a Streamlit dashboard for interactive data visualization.

# Project Overview - Data visualization
Features
Provides an interactive Streamlit dashboard to filter and visualize movie data.
Connects to TiDB Cloud (MySQL-based database) for efficient data storage and retrieval.

Technologies Used
Python (for scripting and automation)
Streamlit (for building the interactive dashboard)
MySQL (TiDB Cloud) (for storing and querying movie data)
Matplotlib & Seaborn (for data visualization)

Steps Involved
1. Set Up Environment
Install Python and required libraries:
2. Run the Scraper
Execute the Python script to scrape movie data from IMDb.
The script navigates the IMDb site, selects genres, and extracts data.
Data is saved in CSV files or inserted into the TiDB Cloud database.
3. Run the Streamlit Dashboard
Start the dashboard using:
streamlit run app.py
Navigate through sections like:
Filtering functions: Filter movies by duration, genre, rating, votes.
Visualizations: Interactive charts for genre distribution, rating trends, vote counts, etc.
