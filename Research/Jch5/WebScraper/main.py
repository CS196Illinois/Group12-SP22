import bs4
import requests

#get website html
req = requests.get('https://plantsam.com/cacti-succulents/')

#clean up with bs4
html = bs4.BeautifulSoup(req.text, "html.parser")

#This should grab all the the things in this class, which should be what we want
content = html.select(".relatedthumb")

images = []
names = []

for item in content:
    try:
        pic = item.find('img')
        images.append(pic['src'])
        names.append(item.text)
    except:
        continue

print(len(names))
print(len(images))


i = 360
print(names[i])
print(images[i])








