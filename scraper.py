from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import pandas as pd 
import pdb

def main():

    url = 'https://okdiario.com/'
    req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})

    webpage = urlopen(req).read()
    page_soup = soup(webpage, "html.parser")
    title = page_soup.find("title")

    #pdb.set_trace() 

    list = []
    df = pd.DataFrame()

    containers = page_soup.findAll("h2","article-title", text=True)
    for container in containers:
        list.append(container.find(text=True).strip())

    df = list
    return df

if __name__ == "__main__":
    df = main()
    print(df)





    

