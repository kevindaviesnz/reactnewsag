from bs4 import BeautifulSoup
import json
import requests
import boto3

s3_client = boto3.client('s3')

def lambda_handler(event, context):

    url = event["presigned_url"]
    response = requests.get(event["url"])
    response.raise_for_status()  # Raise an exception for bad status codes
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')
    tag = event["tag"]
    
    # Store articles in a bucket
    bucket = "kdaviesnz-news-bucket"

    # Extract the text content directly into the array
    elements_data = [element.prettify() for element in soup.find_all(tag)]
    print(elements_data)
    
    # Convert elements_data to JSON string
    json_data = json.dumps(elements_data)

    # Convert JSON string to bytes
    data_bytes = json_data.encode('utf-8')

    # Generate a unique S3 key for the articles
    s3_key = f'kdaviesnz.{url.replace("//", "_").replace(":", "_")}.json'

    # Upload HTML content to S3
    s3_client.put_object(Body=data_bytes, Bucket=bucket, Key=s3_key)

    # Generate a presigned URL for the S3 object
    articles_url = s3_client.generate_presigned_url(
        'get_object',
        Params={'Bucket': bucket, 'Key': s3_key},
        ExpiresIn=3600  # URL expiration time (e.g., 1 hour)
    )

    return {
        'statusCode': 200,
        'articles_url': articles_url,
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
