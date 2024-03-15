from bs4 import BeautifulSoup
import json

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
    # Use list() to convert the map object to a list
    parsed_articles = list(filter(None, map(foxnews_parse_article_content, event["articles"])))
    return {
        'statusCode': 200,
        'articles': [{"uuid":"hello", "headline":"hey there!", "ttl":"5000"}], # parsed_articles,
        'tag': event['tag']
    }


if __name__ == "__main__":
    event = {
        "articles": ["<html><body><header><a href='/some-uri' data-omtr-intcmp='some-uuid'>Headline Text</a></header></body></html>", "<html><body>No Header Here</body></html>"],
        "tag": "p"        
    }
    parsed_articles = lambda_handler(event=event, context=None)
    print(parsed_articles)
