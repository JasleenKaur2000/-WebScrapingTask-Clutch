from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
import pandas as pd

data=[]
r=range(0,2)


for i in r:
    driver=webdriver.Chrome()
    #url="https://clutch.co/web-developers/india?page={}"
    driver.maximize_window()
    driver.get("https://clutch.co/web-developers/india?page={}".format(i))

    time.sleep(5)
    content=driver.page_source.encode('utf-8').strip()
    soup=BeautifulSoup(content,'lxml')

    if i==0:
        jobs=soup.findAll('li',class_="provider provider-row sponsor")
    else:
        jobs=soup.findAll('li',class_="provider provider-row")

    

    for job in jobs:
        company=job.find('a',class_="company_title directory_profile").text.strip()
        employees=job.findAll('div',class_="list-item custom_popover")
        rating=job.find('span',class_="rating sg-rating__number").text.strip()
        salary=employees[0].span.text.replace(' ','')
        employeeNum=employees[1].span.text.replace(' ','')
        location=employees[2].span.text.replace(' ','')
        item={"Company Name":company,"Salary":salary,"Rating":rating,"Employee Size":employeeNum,"Location":location}
        data.append(item)
        print(item)


    driver.quit()


p=pd.DataFrame(data)
p.to_excel("res.xlsx")