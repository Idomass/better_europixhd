#! /usr/bin/env python3
import requests
from bs4 import BeautifulSoup
from constants import URL
from decorators import retry
from media import Media, Movie, TVShow


class API:
    @staticmethod
    @retry
    def autocomplete(query: str) -> [Media]:
        '''
        This function recives a query, and returns
        a list of Media objects
        '''
        soup = BeautifulSoup(requests.post(URL.AUTOCOMPLETE,
                                           data={'query': query}).text, 'html.parser')

        return [Media.create_media(entry.center.contents[0], entry["href"], entry.img["src"])
                for entry in soup.find_all('a')]
