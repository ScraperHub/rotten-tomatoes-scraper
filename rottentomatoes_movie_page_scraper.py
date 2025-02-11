from crawlbase import CrawlingAPI
from bs4 import BeautifulSoup
import json

# Initialize Crawlbase API with your token
crawling_api = CrawlingAPI({'token': 'CRAWLBASE_JS_TOKEN'})

def fetch_html(url):
    options = {
        'ajax_wait': 'true',
        'page_wait': '5000'
    }
    response = crawling_api.get(url, options)
    if response['headers']['pc_status'] == '200':
        return response['body'].decode('utf-8')
    else:
        print(f"Failed to fetch data. Status code: {response['headers']['pc_status']}")
        return None

def fetch_movie_details(movie_url):
    html = fetch_html(movie_url)
    if html:
        soup = BeautifulSoup(html, 'html.parser')

        # Extract movie title
        title = soup.select_one('h1[slot="titleIntro"]').text.strip()

        # Extract synopsis
        synopsis = soup.select_one('div.synopsis-wrap rt-text:not(.key)').text.strip() if soup.select_one('div.synopsis-wrap rt-text:not(.key)') else 'N/A'

        # Get all movie details
        movie_details = {dt.text.strip(): ', '.join([item.text.strip() for item in dd.find_all(['rt-link', 'rt-text']) if item.name != 'rt-text' or 'delimiter' not in item.get('class', [])]) for dt, dd in zip(soup.select('dt.key rt-text'), soup.select('dd'))}

        # Return the collected details as a dictionary
        return {
            'title': title,
            'synopsis': synopsis,
            'movie_details': movie_details
        }
    else:
        print("Failed to fetch movie details.")
        return None

def save_movie_details_to_json(movie_data, filename='movie_details.json'):
    with open(filename, 'w') as file:
        json.dump(movie_data, file, indent=4)
    print(f"Movie details saved to {filename}")

if __name__ == "__main__":
    movie_url = 'https://www.rottentomatoes.com/m/beetlejuice_beetlejuice'
    movie_details = fetch_movie_details(movie_url)
    if movie_details:
        save_movie_details_to_json(movie_details)