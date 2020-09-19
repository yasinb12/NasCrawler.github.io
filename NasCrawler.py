#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 20:38:50 2020

@author: yasinb
"""

# Import libraries
import requests
from bs4 import BeautifulSoup
import time
import urllib.request
from urllib.request import Request, urlopen




# Set the URL you want to webscrape from
url = 'http://www.lyricsondemand.com/n/naslyrics/index.html'

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")

#print(soup)


span = (soup.select('a[href*="lyrics.html"]'))


link = ""
line_count = 1

#Goes through each link and returns HTMl as plaintext

for a in span:
    if (line_count <= 240):
        target = "http://www.lyricsondemand.com/n/naslyrics/" + a['href']
        print(target)
        
        req = Request(target, headers={'User-Agent': 'XYZ/3.0'})
        webpage = urlopen(req, timeout=10).read()
        print("\n")
        soup2 = BeautifulSoup(webpage, "html.parser")
        lyrics = soup2.get_text()
        print(lyrics)
        time.sleep(1)
    line_count += 1
