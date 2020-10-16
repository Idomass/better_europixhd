#! /usr/bin/env python3
import requests
from bs4 import BeautifulSoup
from constants import *


class Media:
    def __init__(self, name, url, img):
        self.name = name
        self.url = url
        self.img = img

    def __str__(self):
        return "Name: {name}\nURL: {url}\nImage source: {img}".format(
            name=self.name, url=self.url, img=self.img)


class API:
    def __init__(self):
        self.headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'sec-ch-ua': '\"Chromium\";v=\"86\", \"\\\"Not\\\\A;Brand\";v=\"99\", \"Google Chrome\";v=\"86\"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'x-requested-with': 'XMLHttpRequest'
        }

    def autocomplete(self, query: str) -> [Media]:
        '''
        This function recives a query, and returns
        a list of Media objects
        '''
        soup = BeautifulSoup(requests.post(AUTOCOMPLETE_URL,
                                           data={'query': query}).text, 'html.parser')

        return [Media(entry.center.contents[0], entry["href"], entry.img["src"])
                for entry in soup.find_all('a')]
