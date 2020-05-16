import requests as req
from bs4 import BeautifulSoup as b

r = req.get("https://www.google.com")

c = r.content
# print(c)

# get the Beautiful soup constructor
soup = b(c, "html.parser")

# prettify the xml content
print(soup.prettify())

print('------------------------------------------------------------------------------------')
# get all the link from the xml
for links in soup.findAll("a"):
    print(links.get("href"))
