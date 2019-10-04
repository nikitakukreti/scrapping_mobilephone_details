import requests
from bs4 import BeautifulSoup
import pandas as pd
l=[]
user={'UserAgent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
page=requests.get('https://www.flipkart.com/mobile-phones-store',headers=user)
soup=BeautifulSoup(page.content,'html.parser')

names=[]
off=[]
mobile_price=[]
phonenames=soup.find_all(class_='iUmrbN')
for name in phonenames:
    names.append(name.getText())
    
offers=soup.find_all(class_='BXlZdc') 
for offer in offers:
    off.append(offer.getText())
    
prices=soup.find_all(class_='_3o3r66') 
for price in prices:
    mobile_price.append(price.getText())

details=pd.DataFrame({'phonenames':names,'offers':off,'prices':mobile_price})

details.to_csv("mobilescrapping.csv")
print("Data has been successfully loaded in CSV file!!")
