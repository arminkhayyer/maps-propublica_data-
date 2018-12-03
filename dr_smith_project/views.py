from django.shortcuts import render,redirect
from django_pandas.io import read_frame
import pandas as pd
import json




def home(request):
    df = pd.read_csv("../cl.csv")
    df= df.to_json()
    return render(request, "maps.html", {"data":df})
