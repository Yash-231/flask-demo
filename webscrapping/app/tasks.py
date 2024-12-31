from urllib import request
from bs4 import BeautifulSoup
import lxml
import time

def count_words(url):
    print(f"Counting words at {url}")
    r=request.urlopen(url)
    soup = 