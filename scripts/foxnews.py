def foxnews_parse_article_content(article_element):
    article_container = {}
    heading_tag = article_element.find("header")
    if heading_tag:
        article_container["uri"] = f"http:{heading_tag.find('a').get('href')}"
        article_container["headline"] = heading_tag.find("a").get_text()
    picture_tag = article_element.find('picture')
    if picture_tag:
        image_tag = picture_tag.find('img')
        article_container["images"] = [f"http:{image_tag.get('data-src')}"]
    return article_container
