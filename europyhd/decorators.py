from time import sleep
from functools import wraps


def retry(func, n = 3):
    @wraps(func)
    def _retry(*args, **kwargs):
        for _ in range(n):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(e)
                print("{0} has failed, retrying..".format(func.__name__))
                sleep(1)
    return _retry
            