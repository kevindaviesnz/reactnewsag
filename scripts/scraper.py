
from bs4 import BeautifulSoup
from typing import List, Dict
import requests

"""
# Example usage:
url = "https://example.com"
html_content = fetch_html(url)
if html_content:
    print(html_content)  # Print or use the HTML content as needed
"""

def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        html_content = response.text
        return html_content
    except requests.exceptions.RequestException as e:
        print("Error fetching HTML:", e)
        return None

def foxnews_parse_article_content(article_container_html):
    article_container = {}
    # bs4.element.Tag
    print("============== Article container starts =========")
    print(type(article_container_html))
    # article_soup = BeautifulSoup(article_container_html, features="html.parser")
    #images = article_soup.find_all("picture")
    print("============== Article container ends =========")
    return article_container_html

def foxnews_get_article_containers(soup):
    # Finds all <article> elements that have a data-card-type attribute. Assign the result to the variable 
    # article_containers, and annotate article_containers to be a list of dictionaries.
    # soup.find_all() returns a bs4.element.ResultSet
    article_containers: List[dict] = list(
        map(foxnews_parse_article_content, soup.find_all("article"))
    )
    return article_containers


if __name__ == "__main__":
    html = fetch_html("https://www.foxnews.com/")
    #print(html)
    # @see https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    soup = BeautifulSoup(html, features="html.parser")
    # print(soup.prettify())
    # print(soup.article)
    foxnews_articles = foxnews_get_article_containers(soup)
    # print(foxnews_articles[0])