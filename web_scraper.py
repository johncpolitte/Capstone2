from pymongo import MongoClient
import time
import random

#Import beautiful soup
import requests
import re
from bs4 import BeautifulSoup
import argparse

client = MongoClient()
database = client['capstone']   # Database name
mongo_connect = database['onion']

links = requests.get('https://www.theonion.com/c/news-in-brief')
soup2 = BeautifulSoup(links.text, 'lxml')


def scrape(soup_object):
    '''
    INPUT:
        -soup_object: BeautifulSoup object
    OUTPUT:
        -Dictioary to mongo db
            Dictionary is in the form of url:article content.
            Each article is stored in mongo as its own dict
        -string: link for more articles button at bottom of the page
    '''
    linkers = soup_object.find_all('h1')
    linkers[0].a['href']
    https = []
    for idx, x in enumerate(linkers):
        https.append(linkers[idx].a['href'])
    for link in https:
        onions = {}
        page = requests.get(link)
        soup = BeautifulSoup(page.text, 'lxml')
        content = soup.find_all('div', {'class':'post-content entry-content js_entry-content '})[0].text
        onions[link] = content[0:-13]
        mongo_connect.insert_one(onions)
        time.sleep(20)

        
    button = soup2.find_all('div', {'class': 'sc-1uzyw0z-0 kiwkfc'})
    more_button = button[0].a['href']
    return 'https://www.theonion.com/c/news-in-brief' + more_button

scrape(soup2)
