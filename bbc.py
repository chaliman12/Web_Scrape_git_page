import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

def get_topics_page():
    topics_url = 'https://www.bbc.com/afaanoromoo'
    response = requests.get(topics_url)
    if response.status_code != 200:
        raise Exception('Failed to load page {}'.format(topics_url))
    doc = BeautifulSoup(response.text, 'html.parser')
    return doc
def get_topic_titles(doc):
    selection_class = 'focusIndicatorDisplayInlineBlock bbc-1mirykb ecljyjm0'
    topic_title_tags = doc.find_all('a', {'class': selection_class})
    topic_titles = []
    for tag in topic_title_tags:
        topic_titles.append(tag.text)
    return topic_titles
def get_topic_descs(doc):
    desc_selector = 'bbc-idwms3 e1mklfmt0'
    topic_desc_tags = doc.find_all('time', {'class': desc_selector})
    topic_descs = []
    for tag in topic_desc_tags:
        topic_descs.append(tag.text.strip())
    return topic_descs
desc=get_topic_descs(get_topics_page())

def get_topic_urls(doc):
    topic_link_tags = doc.find_all('a', {'class': 'focusIndicatorDisplayInlineBlock bbc-1mirykb ecljyjm0'})
    topic_urls = []
    base_url = 'https://www.bbc.com/'
    for tag in topic_link_tags:
        topic_urls.append(base_url + tag['href'])
    return topic_urls


def scrape_topics():
    topics_url = 'https://www.bbc.com/afaanoromoo'
    response = requests.get(topics_url)
    if response.status_code != 200:
        raise Exception('Failed to load page {}'.format(topic_url))
    doc = BeautifulSoup(response.text, 'html.parser')
    topics_dict = {
        'title': get_topic_titles(doc),
        'description': get_topic_descs(doc),
        'url': get_topic_urls(doc)
    }
    topic_df=pd.DataFrame(topics_dict)
    return topic_df.to_csv('bbc.csv',index=None)
scrape_topics()   

  





