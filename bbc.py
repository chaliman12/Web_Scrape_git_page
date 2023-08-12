import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_news_page():
    news_url = 'https://www.bbc.com/afaanoromoo'
    response = requests.get(news_url)
    if response.status_code != 200:
        raise Exception('Failed to load page {}'.format(news_url))
    doc = BeautifulSoup(response.text, 'html.parser')
    return doc
def get_news_titles(doc):
    selection_class = 'focusIndicatorDisplayInlineBlock bbc-1mirykb ecljyjm0'
    news_title_tags = doc.find_all('a', {'class': selection_class})
    news_titles = []
    for tag in news_title_tags:
        news_titles.append(tag.text)
    return news_titles
def get_news_descs(doc):
    desc_selector = 'bbc-idwms3 e1mklfmt0'
    news_desc_tags = doc.find_all('time', {'class': desc_selector})
    news_descs = []
    for tag in news_desc_tags:
        news_descs.append(tag.text.strip())
    return news_descs
def get_news_urls(doc):
    url_class= 'focusIndicatorDisplayInlineBlock bbc-1mirykb ecljyjm0'
    topic_link_tags = doc.find_all('a', {'class':url_class})
   
    news_urls = []
    base_url = 'https://www.bbc.com/'
    for tag in topic_link_tags:
        news_urls.append(base_url + tag['href'])
    return news_urls
def scrape_news():
    news_url = 'https://www.bbc.com/afaanoromoo'
    response = requests.get(news_url)
    if response.status_code != 200:
        raise Exception('Failed to load page {}'.format(news_url))
    doc = BeautifulSoup(response.text, 'html.parser')
    news_dict = {
        'Mata_duree': get_news_titles(doc),
        'Turtii_yeroo': get_news_descs(doc),
        'Liinkii': get_news_urls(doc)
    }
    news_df=pd.DataFrame(news_dict)
    print("Scraping for BBC Afaan Oromoo...") 
    return news_df.to_csv('Oduu_Ammee.csv',index=None)
scrape_news()   






