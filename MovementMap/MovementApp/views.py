from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
import json


def index(request):
    return render(request, 'MovementApp/index.html')


def submit(request):
    with open('/Users/admin/Desktop/wards.json') as f:
      txt = f.read()
    text = json.loads(txt)
    wards = text["features"]
    l = []
    for dic in wards:
        new_dict = {"Name": dic["properties"]["wd16nm"], "ID": dic["properties"]["wd16cd"],
                    "Coordinates": dic["geometry"]["coordinates"][0][0]}
        l.append(new_dict)

    result = {'rubbish data': l}

    return HttpResponseRedirect('/', context=result)



