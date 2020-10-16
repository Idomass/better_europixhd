#! /usr/bin/env python3
from europixhd_api import API

if __name__ == '__main__':
    print(API().autocomplete('avatar')[0])
