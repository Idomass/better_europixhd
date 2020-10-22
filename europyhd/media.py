import requests
from constants import *
from abc import abstractmethod
from decorators import retry
from bs4 import BeautifulSoup
import re


class Media:
    def __init__(self, name, url, img):
        self.url = self.fix_url(url)
        self.name = self.extract_name(name)
        self.img = img

    def __str__(self):
        return f'Name: {self.name}\nURL: {self.url}\nImage source: {self.img}'

    @staticmethod
    def media_factory(name: str, url: str, img: str):
        '''
        This factory function creates a Movie/TVShow and returns it
        '''
        return Movie(name, url, img) if URL.MOVIE in url else TVShow(name, url, img)

    @abstractmethod
    def extract_name(self, name: str) -> str:
        '''
        This function extracts the name from
        the page's meta-data name
        '''
        pass

    @abstractmethod
    def fix_url(self, url) -> str:
        '''
        This function recives url and returns the
        fixed url
        '''
        pass

    @abstractmethod
    @retry
    def get_video(self, season, episode) -> str:
        '''
        This function uses the class information
        in order to get a video link
        '''
        pass


class Movie(Media):
    def __str__(self):
        return 'Type: Movie\n' + super().__str__()

    def extract_name(self, name: str) -> str:
        return re.search(REGEX.MOVIE_NAME, self.url)[1]

    def fix_url(self, url: str) -> str:
        return URL.BASE + url.replace(URL.MOVIE, URL.MOVIE_FIXED)

    @retry
    def get_video(self, *args) -> str:
        soup = BeautifulSoup(requests.post(self.url).text, 'html.parser')

        return URL.BASE + \
            re.search(REGEX.MOVIE, soup.find(
                'div', {'id': 'opis'}).script.prettify())[2]


class TVShow(Media):
    def __str__(self):
        return 'Type: TV Show\n' + super().__str__()

    def extract_name(self, name: str) -> str:
        return re.search(REGEX.SERIES_NAME, self.url)[1]

    def fix_url(self, url: str) -> str:
        return URL.BASE + url.replace(URL.TV_SHOW, URL.TV_SHOW_FIXED)

    @retry
    def get_video(self, season: int, episode: int) -> str:
        return URL.SERIES_WATCH.format(season, episode, name=self.name)
