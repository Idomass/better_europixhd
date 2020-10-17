#! /usr/bin/env python3
from europixhd_api import API

if __name__ == '__main__':
    print(API.autocomplete('brooklyn')[0].get_video(7, 13))
    