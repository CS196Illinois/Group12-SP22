import csv
import random
#from multiprocessing import context
#from django.shortcuts import render

with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)


names = []
links = []

for i in range(len(data)):
    names.append(data[i][0])
    links.append(data[i][1])


index = random.randint(0, len(data))
print(names[index])
print(links[index])


def index(request):
    plant = {'name' : data[index], 'image' : data[index]}
    context = {'plant' : plant}
    #return render(request, 'HTML Here', context)

