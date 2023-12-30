import crawl
import value

url = value.url
tag = value.tag
path_urls = value.path_urls
path_text = value.path_text

# texts = crawl.crawling_print(url, tag)
texts = crawl.crawling_file(path_urls, path_text, url, tag)