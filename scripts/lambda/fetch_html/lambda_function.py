import requests
import json
import boto3

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    
    url = event["url"]
    response = requests.get(event["url"])
    response.raise_for_status()  # Raise an exception for bad status codes
    html_content = response.text
    bucket = "kdaviesnz-news-bucket"
    # Generate a unique S3 key for the HTML content
    s3_key = f'kdaviesnz.{url.replace("//", "_").replace(":", "_")}.html'

    # Upload HTML content to S3
    s3_client.put_object(Body=html_content, Bucket=bucket, Key=s3_key)

    # Generate a presigned URL for the S3 object
    presigned_url = s3_client.generate_presigned_url(
        'get_object',
        Params={'Bucket': bucket, 'Key': s3_key},
        ExpiresIn=3600  # URL expiration time (e.g., 1 hour)
    )
    
    return {
        'statusCode': 200,
        'presigned_url':presigned_url,
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