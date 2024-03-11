
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



def nzherald_get_article_containers(soup):
    # Finds all <article> elements that have a data-card-type attribute. Assign the result to the variable 
    # article_containers, and annotate article_containers to be a list of dictionaries.
    article_containers: List[dict] = soup.find_all("article", attrs={"data-test-ui": True})
    print(article_containers[0])
    """
    article_containers = list(
        filter(
            # Defines a lambda function that takes an argument x and returns True if 
            # "https://www.nzherald.co.nz/" is present in the value associated with the key "src"
            # in the dictionary x. This lambda function will be used as the filtering condition.
            lambda x: "story-card__content" in x["class"],
            article_containers,
        )
    )

    """

#    print(article_containers)
    #output_image_url_list: List[str] = extract_image_urls(images_urls)
    # return output_image_url_list

if __name__ == "__main__":
    html = fetch_html("https://www.foxnews.com/")
    print(html)
    soup = BeautifulSoup(html, features="html.parser")
    nzherald_get_article_containers(soup)