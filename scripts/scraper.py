
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
    # soup.find_all() returns a bs4.element.ResultSet
    article_containers: List[dict] = list(
        map(parse_fn, soup.find_all(tag))
    )
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