from lxml import html
import json

def foxnews_parse_article_content(article_element: str):
    tree = html.fromstring(article_element)
    
    # Use XPath to find the heading tag and other elements
    heading_tag = tree.xpath("//header")[0] if tree.xpath("//header") else None
    a_tag = heading_tag.xpath(".//a[@data-omtr-intcmp]") if heading_tag is not None else None
    
    if a_tag:
        a_tag = a_tag[0]  # Assuming we only care about the first matching <a>
        uri = a_tag.get('href')
        uuid_base = a_tag.get("data-omtr-intcmp")
        uri_suffix = uri.rsplit("/", 1)[-1].replace("-", "_")

        article_container = {
            "uri": uri,
            "headline": a_tag.text,
            "uuid": f"{uuid_base}{uri_suffix}",
            "categories": [uri.split("/")[3] if len(uri.split("/")) > 3 else None],
            'ttl': 86400,  # 24 hours
        }

        # Adjusted to use XPath for finding picture and img tags
        picture_tag = tree.xpath('//picture')[0] if tree.xpath('//picture') else None
        if picture_tag:
            image_tag = picture_tag.xpath('.//img')[0] if picture_tag.xpath('.//img') else None
            src = image_tag.get('data-src') if image_tag is not None else None
            article_container["images"] = [f"http:{src}"] if src else []

        return article_container
    else:
        return ""

def lambda_handler(event, context):
    # Use list() to convert the map object to a list
    parsed_articles = list(map(foxnews_parse_article_content, event["containers"]))
    return {
        'statusCode': 200,
        'containers': json.dumps(parsed_articles, ensure_ascii=False),
        'tag': event['tag']
    }

if __name__ == "__main__":
    event = {
        "containers": ["<html><body><header><a href='/some-uri' data-omtr-intcmp='some-uuid'>Headline Text</a></header></body></html>", "<html><body>No Header Here</body></html>"],
        "tag": "p"        
    }
    parsed_articles = lambda_handler(event=event, context=None)
    print(parsed_articles)
