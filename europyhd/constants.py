class URL:
    BASE = 'https://europixhd.pro/'
    AUTOCOMPLETE = BASE + 'autotesttwn.php'
    MOVIE = '/mov/'
    TV_SHOW = '/tvs/'
    MOVIE_FIXED = '/watch-online-movie/'
    TV_SHOW_FIXED = '/watch-online-tvshow/'
    SERIES_WATCH = BASE + '/svop4/newsrv2?search=dwm-{name}-S{:02d}E{:02d}'

class REGEX:
    MOVIE = 'case 1: *src = (\'|")(.*)(\'|");'
    SERIES_NAME = URL.TV_SHOW_FIXED + '(.*)-online/'
    MOVIE_NAME = URL.MOVIE_FIXED + '(.*)-online-'

WATCH_NAME = 'watch.html'
STARS = '************************************************'
WELCOME = STARS + '\nWelcome to Idomass\'s movies/series search engine\n' + STARS
