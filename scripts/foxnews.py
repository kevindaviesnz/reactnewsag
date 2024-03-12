def foxnews_parse_article_content(article_element):
    heading_tag = article_element.find("header")
    if heading_tag is None or heading_tag.find("a").get("data-omtr-intcmp") is None:
        return None
    else:
        article_container = {}
        uri = f"{heading_tag.find('a').get('href')}"
        article_container["uri"] = uri
        article_container["headline"] = heading_tag.find("a").get_text()
        article_container["uuid"] = f'{heading_tag.find("a").get("data-omtr-intcmp")}{uri.rsplit("/", 1)[-1].replace("-", "_")}'
        article_container['categories'] = [uri.split("/")[3] if len(uri.split("/")) > 3 else None]
        article_container['ttl'] = 86400 # 24 hours
        picture_tag = article_element.find('picture')
        if picture_tag:
            image_tag = picture_tag.find('img')
            src = image_tag.get('data-src')
            article_container["images"] = [f"http:{src}"] if src is not None else []
        return article_container
