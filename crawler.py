#!/usr/bin/env python

import requests


def request(url):
    try:
        get_response = requests.get("http://" + url)
        return get_response
    except requests.exceptions.ConnectionError:
        pass


target_url = "10.0.2.12/mutillidae"
target_link = []
with open("/root/Documents/dir.list", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = target_url + "/" + word
        response = request(test_url)
        if response:
            print("[+] Discovered URL --> " + test_url)







