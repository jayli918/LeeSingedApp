from django.shortcuts import render, render_to_response, RequestContext
from .forms import SummonerInputForm
import json
import requests

# Create your views here.
def home(request):
    form = SummonerInputForm (request.POST or None)
    apikey = 'api_key=b574f3e0-1898-4a5f-9454-1cb4d5c5cfb4' 
    host = 'https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/'
    if form.is_valid():
        gege = form['Summoner']
        r = requests.post(host + str(gege.value()),params=apikey)
        print(r.json())
        print(r.url)
    else:
        print("nein!")
    return render_to_response("Front.html",
                              locals(),
                              context_instance= RequestContext(request)
                              )