from bs4 import BeautifulSoup

with open("index.html", "rb") as f:
    doc = BeautifulSoup(f, "html.parser")
#print(doc.prettify())

tags = doc.find_all("p")[0]
#tag.string = "hello"
print(tags.find_all("b"))
