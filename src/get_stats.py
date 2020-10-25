import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

"""
File to scrape 2019-2020 season data, amend problems in dataset and write 
the refined data to a csv file.
"""
# NBA season we will be analyzing
year = 2020
# URL page we will scraping
url = "https://www.basketball-reference.com/leagues/NBA_2020_per_game.html".format(
    year)
# this is the HTML from the given URL
html = urlopen(url)
soup = BeautifulSoup(html, features="html.parser")
# use findALL() to get the column headers
soup.findAll('tr', limit=2)
# use getText()to extract the text we need into a list
headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]
# exclude the first column as we will not need the ranking order from Basketball Reference for the analysis
headers = headers[1:]

# avoid the first header row
rows = soup.findAll('tr')[1:]
player_stats_raw = [[td.getText() for td in rows[i].findAll('td')]
                for i in range(len(rows))]

stats = []
for i in range(len(player_stats_raw)):
    if i == 0:
        stats.append(player_stats_raw[0])
    else:
        if len(player_stats_raw[i]) != 0:
            if stats[len(stats)-1][0] != player_stats_raw[i][0]:
                stats.append(player_stats_raw[i])
     
        
    

data = pd.DataFrame(stats, columns=headers)
data.to_csv('stats.csv', index = False)
