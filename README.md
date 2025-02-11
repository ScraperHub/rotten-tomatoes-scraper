# Rottentomatoes.com Scrapers

## Description

This repository contains Python-based scrapers that extract data from Rotten Tomatoes Movie Listings and Rotten Tomatoes Movie Details pages. The scrapers use the [Crawlbase Crawling API](https://crawlbase.com/crawling-api-avoid-captchas-blocks) to handle CAPTCHA challenges, pagination, anti-bot protections, and JavaScript-rendered content seamlessly.

The extracted data is parsed and saved in JSON format.

➡ For detailed instructions, visit the full blog [here](https://crawlbase.com/blog/how-to-scrape-rotten-tomatoes/).

## Scrapers Overview

### Rottentomatoes.com Movie Listings Scraper

The Rottentomatoes.com Movie Listings Scraper (rottentomatoes_serp_scraper.py) extracts:

1. **Movie Title**
2. **Critics score**
3. **Audience Score**
4. **Movie Page Link**

It also automatically handles pagination, ensuring comprehensive data extraction. It saves the extracted data in a JSON file.

### Rottentomatoes.com Movie Details Page Scraper

The Rottentomatoes.com Movie Details Page Scraper (rottentomatoes_movie_page_scraper.py) extracts detailed movie information, including:

1. **Movie Title**
2. **Synopsis**
3. **Movie Details like Director, Producer, Screenwriter, Distributor, rating etc**

It saves the extracted data in a JSON file.

## Environment Setup

Ensure that Python is installed on your system. Check the version using:

```bash
# Use python3 if you're on Linux with Python 3 installed
python --version
```

Next, install the required dependencies:

```bash
pip install crawlbase beautifulsoup4
```

- **Crawlbase** – Handles JavaScript rendering and bypasses bot protections.
- **BeautifulSoup** – Parses and extracts structured data from HTML.

## Running the Scrapers

1. **Get Your Crawlbase Access Token**

   - Sign up for Crawlbase [here](https://crawlbase.com/signup) to get an API token.
   - Use the JS token for Rottentomatoes.com scraping, as the site uses JavaScript-rendered content.

2. **Update the Scraper with Your Token**

   - Replace `"CRAWLBASE_JS_TOKEN"` in the script with your Crawlbase JS Token.

3. **Run the Scraper**

```bash
# Use python3 if required (for Linux/macOS)
python SCRAPER_FILE_NAME.py
```

Replace `"SCRAPER_FILE_NAME.py"` with the actual script name (`rottentomatoes_serp_scraper.py` or `rottentomatoes_movie_page_scraper.py`).

## To-Do List

- Expand scrapers to extract additional movie details.
- Optimize data storage and export formats (e.g., CSV, database integration).
- Enhance scraper efficiency and speed.

## Why Use These Scrapers?

- **Extracts Rotten Tomatoes Data** efficiently.
- **Bypasses CAPTCHAs and anti-bot protections** with Crawlbase.
- **Handles JavaScript-rendered content** seamlessly.
- **Supports easy pagination** for scraping multiple pages.
