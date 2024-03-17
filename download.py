#!/usr/bin/env python

import requests


def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)


download("https://upload.wikimedia.org/wikipedia/commons/f/f0/Nissan_GTR.jpg")