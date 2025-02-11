from crawlbase import CrawlingAPI
from bs4 import BeautifulSoup
import json

# Initialize Crawlbase API with your token
crawling_api = CrawlingAPI({'token': 'CRAWLBASE_JS_TOKEN'})

def fetch_html_with_pagination(url):
    options = {
        'ajax_wait': 'true',
        'page_wait': '5000',
        'css_click_selector': 'button[data-qa="dlp-load-more-button"]'  # CSS Selector for "Load More" button
    }
    response = crawling_api.get(url, options)
    if response['headers']['pc_status'] == '200':
        return response['body'].decode('utf-8')
    else:
        print(f"Failed to fetch data. Status code: {response['headers']['pc_status']}")
        return None

def parse_movies(html):
    soup = BeautifulSoup(html, 'html.parser')
    movies = soup.select('div[data-qa="discovery-media-list"] > div.flex-container')

    movie_data = []
    for movie in movies:
        title = movie.select_one('span[data-qa="discovery-media-list-item-title"]').text.strip() if movie.select_one('span[data-qa="discovery-media-list-item-title"]') else ''
        criticsScore = movie.select_one('rt-text[slot="criticsScore"]').text.strip() if movie.select_one('rt-text[slot="criticsScore"]') else ''
        audienceScore = movie.select_one('rt-text[slot="audienceScore"]').text.strip() if movie.select_one('rt-text[slot="audienceScore"]') else ''
        link = movie.select_one('a[data-qa^="discovery-media-list-item"]')['href'] if movie.select_one('a[data-qa^="discovery-media-list-item"]') else ''

        movie_data.append({
            'title': title,
            'critics_score': criticsScore,
            'audience_score': audienceScore,
            'link': 'https://www.rottentomatoes.com' + link
        })

    return movie_data

def save_to_json(data, filename='movies.json'):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    url = 'https://www.rottentomatoes.com/browse/movies_in_theaters/sort:top_box_office'
    html_content = fetch_html_with_pagination(url)
    if html_content:
        movies_data = parse_movies(html_content)
        save_to_json(movies_data)