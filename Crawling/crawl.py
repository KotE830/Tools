import requests
from bs4 import BeautifulSoup

def crawling(url, tag):
  html = requests.get(url).text
  soup = BeautifulSoup(html, 'html.parser')
  return soup.select(tag)

# print on terminal
def crawling_print(url, tag):
  for text in crawling(url, tag):
    print(text.text)

# print on file
def crawling_file(path_urls, path_text, url, tag):
  urls = open(path_urls, 'r')
  textfile = open(path_text, 'w', encoding='UTF-8')

  for url in urls.readlines():
    try:
      for text in crawling(url, tag):
        textfile.write(text.text + '\n')
    except:
      pass

  urls.close()
  textfile.close()