import requests as req

r = req.get("https://www.google.com")

c = r.content
print(c)
