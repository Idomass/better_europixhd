class URL:
    BASE = 'https://europixhd.io/'
    AUTOCOMPLETE = BASE + 'autotest.php'
    MOVIE = '/mov/'
    TV_SHOW = '/tvs/'
    MOVIE_FIXED = '/watch-online-movie/'
    TV_SHOW_FIXED = '/watch-online-tvshow/'
    SERIES_WATCH = BASE + '/svop4/newsrv2?search=dwm-{name}-S{:02d}E{:02d}'

MOVIE_REGEX = 'case 1: *src = (\'|")(.*)(\'|");'
SERIES_NAME_REGEX = URL.TV_SHOW_FIXED + '(.*)-online/'



