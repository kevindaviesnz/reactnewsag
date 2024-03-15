from bs4 import BeautifulSoup
import json
import requests


def foxnews_parse_article_content(article_element: str):
    soup = BeautifulSoup(article_element, 'html.parser')
    
    # Find the heading tag and a tag within it
    heading_tag = soup.find('header')
    a_tag = heading_tag.find('a', {'data-omtr-intcmp': True}) if heading_tag else None
    
    if a_tag:
        uri = a_tag.get('href')
        uuid_base = a_tag.get("data-omtr-intcmp")
        uri_suffix = uri.rsplit("/", 1)[-1].replace("-", "_")

        article_container = {
            "uri": uri,
            "headline": a_tag.text.strip(),
            "uuid": f"{uuid_base}{uri_suffix}",
            "categories": [uri.split("/")[3] if len(uri.split("/")) > 3 else None],
            'ttl': 86400,  # 24 hours
        }

        # Find picture and img tags
        picture_tag = soup.find('picture')
        if picture_tag:
            image_tag = picture_tag.find('img')
            src = image_tag.get('data-src') if image_tag else None
            article_container["images"] = [f"http:{src}"] if src else []

        return article_container
    else:
        return None

def lambda_handler(event, context):
    
    response = requests.get(event["articles_url"])
    response.raise_for_status()  # Raise an exception for bad status codes
    articles_content = response.text

    # Use list() to convert the map object to a list
    # parsed_articles = list(filter(None, map(foxnews_parse_article_content, articles_content)))
    parsed_articles = articles_content
    return {
        'statusCode': 200,
        'articles': parsed_articles,
        'tag': event['tag']
    }


if __name__ == "__main__":
    event = {
        "articles_url": "https://kdaviesnz-news-bucket.s3.amazonaws.com/kdaviesnz.https__kdaviesnz-news-bucket.s3.amazonaws.com/kdaviesnz.https__foxnews.com.html%3FAWSAccessKeyId%3DAKIA42RD47OJM3V6Q2HU%26Signature%3DayMaHoDJo4%252B%252F%252F%252F8cGQmwfJ5Jrs4%253D%26Expires%3D1710708201.json?AWSAccessKeyId=AKIA42RD47OJM3V6Q2HU&Signature=9HOWKwRLfDS8NSbJ%2BTNBowB14X0%3D&Expires=1710708523",
        "tag": "p"        
    }
    parsed_articles = lambda_handler(event=event, context=None)
    print(parsed_articles)
