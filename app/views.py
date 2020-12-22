from django.shortcuts import render
from django import forms

class NewTaskForm(forms.Form):
    task = forms.CharField(label="Player:")


# Create your views here.
def index(request):
    return render(request, "app/index.html")


def player(request):
    return render(request, "app/player.html")
