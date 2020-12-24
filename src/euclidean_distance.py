import csv
from math import sqrt
from typing import List

import pandas as pd

"""
Create vectors for each player and calculate the distance between each vector
"""
# #Stats Dataframe
# stats = pd.read_csv('stats.csv')
# stats = stats.drop(columns=['Pos', "Age", "Tm", "G", "GS"])
# stats = stats.fillna(0)
# stats.set_index('Player', inplace=True)
# #Advanced Stats Dataframe
# advanced_stats = pd.read_csv('src/advanced_stats.csv')
# column_names = advanced_stats.columns.values
# column_names[18] = "delete"
# column_names[23] = "delete2"
# advanced_stats.columns = column_names
# advanced_stats = advanced_stats.drop(columns=["Pos", "Age", "Tm", "G", "delete", "delete2"])
# advanced_stats.set_index('Player', inplace=True)

def get_distance(player1: List, player2: List) -> float:
    distance_squared = 0
    for i in range(len(player1)):
        d = abs(player1[i] - player2[i]) ** 2
        distance_squared += d
    return sqrt(distance_squared)

def find_all_similar(player1: List, stats):
    all_similar = {}
    for i, row in stats.iterrows():
        if player1.name != i:
            all_similar[get_distance(player1, stats.loc[i])] = [i]
    return all_similar

def get_most_similar(all_similar):
    smallest = list(all_similar.keys())
    smallest.sort()
    most_similar = []
    counter = 0
    while counter < 5:
       for player in all_similar[smallest[counter]]:
            most_similar.append(player)
            counter +=1
    return most_similar

def player_list(stats):
    lst = []
    for i, row in stats.iterrows():
        lst.append(str(row.name))
    return lst



# a = find_all_similar(stats.loc["Danny Green"], stats)
# b = get_most_similar(a)
