#Scraping clutch 
import requests
from bs4 import BeautifulSoup
import pandas as pd

url='https://clutch.co/web-developers?geona_id=356'

def get_data(url):
    r=requests.get(url)
    soup=BeautifulSoup(r.text,'html.parser')
    return soup

def parse(soup):
    data=soup.find_all('div',{'class':'company col-md-12 prompt-target sponsor'}).text
    print(len(data))
    return
    


soup=get_data(url)
parse(soup)

