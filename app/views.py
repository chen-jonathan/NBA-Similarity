import pandas as pd
from django.shortcuts import render
from django import forms

from src import euclidean_distance

stats = pd.read_csv('src/stats.csv')
stats = stats.drop(columns=['Pos', "Age", "Tm", "G", "GS"])
stats = stats.fillna(0)
stats.set_index('Player', inplace=True)
player_list = euclidean_distance.player_list(stats)


class NameForm(forms.Form):
    player_real_name = forms.CharField(label=False, widget=forms.TextInput(attrs={'list':'player-input'}))


def index(request):
    if request.method == 'POST':

        form = NameForm(request.POST)

        if form.is_valid():  # maybe add if player is in dictionary

            player_name = form.cleaned_data["player_real_name"]
            if player_name in player_list:
                a = euclidean_distance.find_all_similar(stats.loc[player_name],
                                                        stats)
                top_five = euclidean_distance.get_most_similar(a)
                return render(request, 'app/index.html', {
                    'form': form,
                    'player_name': player_name,
                    'submitted': True,
                    "top_five": top_five,
                    "message": "",
                    "datalist": player_list})
            else:
                return render(request, 'app/index.html', {
                    'form': form,
                    'player_name': player_name,
                    'submitted': False,
                    "top_five": [],
                    "message": "Please type in a valid name",
                    "datalist": player_list})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'app/index.html',
                  {'form': form, 'player_name': "", 'submitted': False,
                   "top_five": [], "message": "",
                   "datalist": player_list})
