#! /usr/bin/env python3
import requests
from bs4 import BeautifulSoup, Tag
from constants import URL, WATCH_NAME
from decorators import retry
from media import Media, Movie, TVShow
from os import system


class API:
    @staticmethod
    @retry
    def search(query: str) -> [Media]:
        '''
        This function recives a query, and returns
        a list of Media objects
        '''
        soup = BeautifulSoup(requests.post(URL.AUTOCOMPLETE,
                                           data={'query': query}).text, 'html.parser')

        return [Media.media_factory(entry.center.contents[0], entry['href'], entry.img['src'])
                for entry in soup.find_all('a')]

    @staticmethod
    def watch(media: Media, season: int = 0, episode: int = 0) -> None:
        iframe = API.__iframe_from_url(media.get_video(season, episode))

        with open(WATCH_NAME, 'w') as o_watch:
            o_watch.write(iframe.prettify())

        system(f'google-chrome {WATCH_NAME} > /dev/null 2> /dev/null &')

    @staticmethod
    def __iframe_from_url(url: str) -> Tag:
        return BeautifulSoup(requests.post(url).text, 'html.parser').iframe