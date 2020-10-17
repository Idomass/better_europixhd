import requests
from constants import *
from abc import abstractmethod
from decorators import retry
from bs4 import BeautifulSoup
import re


class Media:
    def __init__(self, name, url, img):
        self.name = name
        self.url = self.fix_url(url)
        self.img = img

    def __str__(self):
        return f'Name: {self.name}\nURL: {self.url}\nImage source: {self.img}'

    @staticmethod
    def create_media(name, url, img):
        '''
        This function creates a Movie/TVShow and returns it
        '''
        return Movie(name, url, img) if URL.MOVIE in url else TVShow(name, url, img)

    @abstractmethod
    def fix_url(self, url) -> str:
        '''
        This function recives url and returns the
        fixed url
        '''
        pass

    @abstractmethod
    @retry
    def get_video(self) -> str:
        '''
        This function uses the class information
        in order to get a video link
        '''
        pass


class Movie(Media):
    def __str__(self):
        return 'Type: Movie\n' + super().__str__()

    def fix_url(self, url: str) -> str:
        return URL.BASE + url.replace(URL.MOVIE, URL.MOVIE_FIXED)

    @retry
    def get_video(self) -> str:
        soup = BeautifulSoup(requests.post(self.url).text, 'html.parser')

        return URL.BASE + \
            re.search(MOVIE_REGEX, soup.find(
                'div', {'id': 'opis'}).script.prettify())[2]


class TVShow(Media):
    def __str__(self):
        return 'Type: TV Show\n' + super().__str__()

    def fix_url(self, url: str) -> str:
        return URL.BASE + url.replace(URL.TV_SHOW, URL.TV_SHOW_FIXED)

    @retry
    def get_video(self, season: int, episode: int) -> str:
        return URL.SERIES_WATCH.format(season, episode,
                                       name=re.search(SERIES_NAME_REGEX, self.url)[1])
