

# Initialize NewsApiClient with your API key
from newsapi import NewsApiClient
import requests
from bs4 import BeautifulSoup

# Initialize NewsApiClient with your API key
newsapi = NewsApiClient(api_key='371a76c13f6c43cb828a1933781f7947')

# Define the search query
query = 'your search query here'

# Search for articles
articles = newsapi.get_everything(q=query, language='en', sort_by='relevancy')

# Print the titles, URLs, and content of the articles
for article in articles['articles']:
    print("Title:", article['title'])
    print("URL:", article['url'])
    
    # Fetch the full content of the article
    response = requests.get(article['url'])
    html_content = response.text
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract text content from the HTML
    text_content = ''
    for paragraph in soup.find_all('p'):
        text_content += paragraph.text + '\n'
    
    # Print the text content of the article
    print("Content:", text_content)
    print()
