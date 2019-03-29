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
mongo_connect = database['onion1']


def scrape(start_link):
    '''
    INPUT:
        -soup_object: starting link for scraping
            'https://www.theonion.com/c/news-in-brief?startTime=1551378420821'
    OUTPUT:
        -Dictioary to mongo db
            Dictionary is in the form of url:article content.
            Each article is stored in mongo as its own dict
        -string: link for more articles button at bottom of the page
    '''
    links = [start_link]
    print(links)
    count = 0
    for link in links:
        print(link)
        soup = requests.get(link)
        if count < 10000:
            soup2 = BeautifulSoup(soup.text, 'lxml')
            linkers = soup2.find_all('h1', {'class': 'headline entry-title'})
            https = []
            for idx, x in enumerate(linkers):
                https.append(linkers[idx].a['href'])
            for link in https:
                onion = {}
                '''
                need to replace . in html with DOT
                '''
                no_dot = link.replace('.', 'DOT')
                page = requests.get(link)
                soup = BeautifulSoup(page.text, 'lxml')
                content = soup.find_all('p')
                content = list(content)
                onion[no_dot] = str(content[0])
                print(count)
                print(onion)
                mongo_connect.insert_one(onion)
                time.sleep(10)
                count += 1

            button = soup2.find_all('div', {'class': 'sc-1uzyw0z-0 kiwkfc'})
            more_button = button[0].a['href']
            links.append('https://www.theonion.com/c/news-in-brief' + more_button)




if __name__ = '__main__':

    start_link ='https://www.theonion.com/c/news-in-brief'
    scrape(start_link)
