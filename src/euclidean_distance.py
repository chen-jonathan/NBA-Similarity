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
player_dictionary = {}
vector = []
for index, row in df.iterrows():
    name = row[0]
    player_dictionary[name] = row[6:].array

lebron = player_dictionary["LeBron James"]
luka = player_dictionary["Luka Dončić"]
ball = player_dictionary["Lonzo Ball"]
rubio = player_dictionary["Ricky Rubio"]
duncan = player_dictionary["Duncan Robinson"]
jj = player_dictionary["J.J. Redick"]
ingram = player_dictionary["Brandon Ingram"]
tatum = player_dictionary["Jayson Tatum"]
wesley = player_dictionary["Wesley Matthews"]
danny = player_dictionary["Danny Green"]
deAndre = player_dictionary["DeAndre Jordan"]
thompson = player_dictionary["Tristan Thompson"]
robert = player_dictionary["Robert Covington"]

# print(lebron[0:])
# print(luka[0:])
# print(get_distance(jj, duncan))
# print(get_distance(lebron, luka))
# print(get_distance(rubio, ball))
print(get_distance(robert, danny))
# print(get_distance(ingram, tatum))
# print(get_distance(deAndre, thompson))



