from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse




class NameForm(forms.Form):
    player_real_name = forms.CharField(label=False)


# Create your views here.


def index(request):
    # Check if method is POST

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():  # maybe add if player is in dictionary
            # process the data in form.cleaned_data as required
            player_name = form.cleaned_data["player_real_name"]
            return render(request, 'app/index.html', {'form': form, 'player_name': player_name, 'submitted': True})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()


    return render(request, 'app/index.html', {'form': form, 'player_name': "", 'submitted': False})



