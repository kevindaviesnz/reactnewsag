from bs4 import BeautifulSoup
import json
import requests

def lambda_handler(event, context):

    url = event["presigned_url"]
    response = requests.get(event["url"])
    response.raise_for_status()  # Raise an exception for bad status codes
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')
    tag = event["tag"]

    # Extract the text content directly into the array
    elements_data = [element.get_text(strip=True) for element in soup.find_all(tag)]

    return {
        'statusCode': 200,
        'articles': elements_data,
        'tag': tag,
        "url": event["url"]
    }

if __name__ == "__main__":
    
    event = {
        "presigned_url": "https://kdaviesnz-news-bucket.s3.amazonaws.com/kdaviesnz.https__foxnews.com.html?AWSAccessKeyId=AKIA42RD47OJILOLQHQO&Signature=30Q2kJVKs2T7Vvp%2B1JOBF%2B4TssU%3D&Expires=1710475837",
        "tag": "article",
        "url": "https://foxnews.com"       
    }
    articles = lambda_handler(event=event, context=None)
    print(articles)
