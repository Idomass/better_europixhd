#! /usr/bin/env python3
from europixhd_api import API, TVShow, Movie
from constants import WELCOME, STARS

def main():
    season, episode = 0, 0

    print(WELCOME)
    while True:
        matches = API.search(input('Search: '))
        if matches == [] or matches is None:
            print('No matches found :(')
            continue
        # print results
        print('0: Abort')
        for id, match in enumerate(matches):
            print(f'{id + 1}: {match.name} ({"TVShow" if type(match) is TVShow else "Movie"})' )
        
        while True:
            selection = int(input('Selection: ')) - 1
            if selection == -1:
                break

            media = matches[selection]
            if isinstance(media, TVShow):
                season, episode = int(input('Season: ')), int(input('Episode: '))
            
            API.watch(media, season, episode)
            break
        print(STARS)


if __name__ == '__main__':
    main()



    API.watch(API.search('avatar')[0], 3, 2)
    