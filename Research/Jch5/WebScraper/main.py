import bs4
import requests

#get website html
req = requests.get('https://plantsam.com/cacti-succulents/')

#clean up with bs4
html = bs4.BeautifulSoup(req.text, "html.parser")

#This should grab all the the things in this class, which should be what we want
content = html.select(".relatedthumb")

#checking what we got...
i = 5
#print((content[i]))
#print(content[0].text)
#print(len(content))


images = []
names = []

"""
So i cant figure out how to get the image tags into the list, i tried to 
isolate the tags with the loop below but for some reason about 20% of the 
images arent being added...
"""


for item in content:
    names.append(item.text)
    itemstring = str(item)
    itemlist = itemstring.split(" ")
    itemlist = itemlist[10:20]

    for elem in itemlist:
        part = elem.split('=')
        if part[0] == "src" or part[0] == "srcset":
            images.append(elem)



print((names[i]))
print((images[i]))








