from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
import pandas as pd

data=[]

driver=webdriver.Chrome()
url="https://clutch.co/web-developers?geona_id=356"
driver.maximize_window()
driver.get(url)

time.sleep(5)
content=driver.page_source.encode('utf-8').strip()
soup=BeautifulSoup(content,'lxml')


companyName=soup.findAll('a',class_='company_title directory_profile')
print(companyName[0].text.strip())

employees=soup.findAll('div',class_="list-item custom_popover")
location=employees[2].span.text.replace(', India','')

print(location)

driver.quit()