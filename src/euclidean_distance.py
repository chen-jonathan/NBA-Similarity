import csv
import pandas as pd
"""
Create vectors for each player and calculate the distance between each vector
"""

df = pd.read_csv('stats.csv')
player_dictionary = {}
vector= []
for index, row in df.iterrows():
    name = row[0]
    player_dictionary[name] = row[4:].array

lebron = player_dictionary["LeBron James"]
luka = player_dictionary["Luka Dončić"]


print(lebron[0:])
print(luka[0:])