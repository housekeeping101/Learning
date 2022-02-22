from bs4 import BeautifulSoup
import requests
import re

item_found = {}

url = f"https://unit42.paloaltonetworks.com/gamaredon-primitive-bear-ukraine-update-2021/"
page = requests.get(url).text
#print(page)
doc = BeautifulSoup(page, "html.parser")
afind = doc.find(class_="article__content pb-30")
for i in afind:
    parent = i.parent
    print(i)
    if parent.name != "span":
        continue
    link = parent['href']
    next = i.find_parent(class_="container")
    print(next)
    ioc = next.find_parent("span")
    item_found[i] = {"ioc": ioc, "link": link}
sor = sorted(item_found.items(), key=lambda x: x[1]['ioc'])
print(sor)
for i in sor:
    print(i[0])
    print(f"${i[1]['ioc']}")
    print(i[1]['link'])
    print("---" * 10)
#items = div.find_all(class_="article__content pb-30")
#print(div)

