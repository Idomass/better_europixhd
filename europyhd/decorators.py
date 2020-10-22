from time import sleep
from functools import wraps
from sys import stderr


def retry(func, n = 3):
    @wraps(func)
    def _retry(*args, **kwargs):
        for _ in range(n):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(e, file=stderr)
                print("{0} has failed, retrying..".format(func.__name__), file=stderr)
                sleep(1)
    return _retry
            