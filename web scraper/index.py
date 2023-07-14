import requests
from bs4 import BeautifulSoup

url = 'https://payway.ug/'
r = requests.get(url)
print(r)

soup = BeautifulSoup(r.content, "lxml")
title = soup.find_all('a', {'class':'sc-cIShpX llOCaz'})
print(title)