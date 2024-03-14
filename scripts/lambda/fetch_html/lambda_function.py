import requests
import json

def lambda_handler(event, context):
    response = requests.get(event["url"])
    response.raise_for_status()  # Raise an exception for bad status codes
    html_content = response.text

    return {
        'statusCode': 200,
        'html': json.dumps(html_content),
        'tag': event["tag"],
        'url': event["url"]
    }


if __name__ == "__main__":
    
    event = {
        "url":"https://foxnews.com",
        "tag":"article"
    }
    foxnews_articles = lambda_handler(event=event, context=None)
    print(foxnews_articles)