import csv
from math import sqrt
from typing import List

import pandas as pd

"""
Create vectors for each player and calculate the distance between each vector
"""
def get_distance(player1: List, player2: List) -> float:
    distance_squared = 0
    for i in range(len(player1)):
        d = abs(player1[i] - player2[i]) ** 2
        distance_squared += d
    return sqrt(distance_squared)

df = pd.read_csv('stats.csv')
df = df.drop(columns=['Pos', "Age", "Tm", "G", "GS"])
df = df.fillna(0)
df.set_index('Player', inplace=True)
lst = df.loc['Steven Adams']
print(lst['MP'])
 
#player_dictionary = {}
#vector= []
#for index, row in df.iterrows():
#    name = row[0]
#    player_dictionary[name] = row[4:].array

#lebron = player_dictionary["LeBron James"]
#luka = player_dictionary["Luka Dončić"]


#print(lebron[0:])
#print(luka[0:])

