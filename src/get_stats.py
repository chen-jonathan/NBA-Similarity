import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# NBA season we will be analyzing
year = 2020
# URL page we will scraping
url = "https://www.basketball-reference.com/leagues/NBA_2020_per_game.html".format(year)
# this is the HTML from the given URL
html = urlopen(url)
soup = BeautifulSoup(html)
