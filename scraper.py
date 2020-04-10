from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import pandas as pd 

url = 'https://okdiario.com/'
req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(req).read()
page_soup = soup(webpage, "html.parser")
title = page_soup.find("title")

list = []
df = pd.DataFrame()

containers = page_soup.findAll("p","article-lead", text=True)
for container in containers:
    list.append(container.find(text=True).strip())

df = list

print(df)