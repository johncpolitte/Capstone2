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
mongo_connect = database['onion_articles']


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
    # Sets the article count at 0
    count = 0
    # Links is the list of pages that will be appended to at the end of
    # the for loop. The links page represents the website from the onion
    # that has 20 links to articles on it. The html code from the more
    # button (next-page) is appended to this list so that it will
    # the links on the next page will also be scrapped
    for link in links:
        print(link)
        # Gets the html code from the onion page with 20 article links on it
        soup = requests.get(link)
        # Going to pull 10,000 articles. This if statement will end the
        # function once the cound reaches 10,000
        if count < 10000:
        # Turns html code from artilce page into beautiful soup object
            soup2 = BeautifulSoup(soup.text, 'lxml')
        # Uses the 'h1' tag to find all of the links for the 20 articles
            linkers = soup2.find_all('h1', {'class': 'headline entry-title'})
        # Initialize a list of all of the web address's for the 20 articles
        # also empties the list when the loop comes back around for the
        # next 20 articles
            https = []
        # For loop that iterates through the list of 20 links of articles,
        # and adds the web address to the https list
            for idx, x in enumerate(linkers):
        # Gets the web address for each artcle and appends it to the list
                https.append(linkers[idx].a['href'])
        # Four loop that goes through the list of 20 articles from the
        # links web page that has 20 articles
            for ar_link in https:
        # Initialize dictionary to insert into mongo
                onion = {}
                '''
                need to replace . in html with DOT
                '''
        # replace '.' with DOT in webaddress so it can be key in dictionary
                no_dot = ar_link.replace('.', 'DOT')
        # Gets html for webpage with the article
                page = requests.get(ar_link)
        # Turns into beautiful soup object
                soup = BeautifulSoup(page.text, 'lxml')
        # Finds the p tag in the object because that is where the acticle text is
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




if __name__ == '__main__':

    start_link ='https://www.theonion.com/c/news-in-brief'
    scrape(start_link)
