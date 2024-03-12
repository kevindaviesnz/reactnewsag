
from bs4 import BeautifulSoup
from typing import List, Dict
from foxnews import foxnews_parse_article_content
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


def get_article_containers(soup, tag, parse_fn):
    """
    Extracts article containers from BeautifulSoup's ResultSet using a specified tag and parsing function.

    :param soup: BeautifulSoup object representing the HTML content
    :param tag: The tag to search for within the soup
    :param parse_fn: A function to parse each found tag and return a dictionary representing the article container
    :return: List of article containers as dictionaries
    """
    # Use a generator expression inside a list comprehension
    article_containers: List[dict] = [
        item for item in (parse_fn(x) for x in soup.find_all(tag)) if item is not None
    ]
    return article_containers



if __name__ == "__main__":
    html = fetch_html("https://www.foxnews.com/")
    #print(html)
    # @see https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    soup = BeautifulSoup(html, features="html.parser")
    # print(soup.prettify())
    # print(soup.article)
    foxnews_articles = get_article_containers(soup=soup, tag="article", parse_fn=foxnews_parse_article_content)
    print(foxnews_articles)