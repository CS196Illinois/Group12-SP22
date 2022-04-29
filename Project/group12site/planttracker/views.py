from encodings import utf_8
import re
from django.shortcuts import render

def home(request):
    return render(request, "planttracker/Boxcomp.html")

def NewUser(request):
    return render(request, "planttracker/NewUser.html")

import csv
import random
from multiprocessing import context

with open('data.csv', 'r', encoding="utf8") as f:
    reader = csv.reader(f)
    data = list(reader)


names = []
links = []

for i in range(len(data)):
    names.append(data[i][0])
    links.append(data[i][1])



def index(request):
    j = random.randint(0, len(data))
    plant1 = {'name' : names[j], 'image' : links[j]}
    k = random.randint(0, len(data))
    plant2 = {'name' : names[k], 'image' : links[k]}
    l = random.randint(0, len(data))
    plant3 = {'name' : names[l], 'image' : links[l]}
    m = random.randint(0, len(data))
    plant4 = {'name' : names[m], 'image' : links[m]}
    n = random.randint(0, len(data))
    plant5 = {'name' : names[n], 'image' : links[n]}
    o = random.randint(0, len(data))
    plant6 = {'name' : names[o], 'image' : links[o]}
    context = {'plant1' : plant1, 'plant2' : plant2, 'plant3' : plant3, 'plant4' : plant4, 'plant5' : plant5, 'plant6' : plant6}
    return render(request, 'planttracker/Boxcomp.html', context)