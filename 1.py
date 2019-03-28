import requests
from fake_useragent import UserAgent
import re
from bs4 import BeautifulSoup
import urllib


url="https://www.consumerreports.org/cro/a-to-z-index/products/index.htm"

#user_agent=UserAgent()

#page=requests.get(url,headers={'user-agent':user_agent.chrome})

page=urllib.request.urlopen(url)

soup=BeautifulSoup(page,'lxml')

element=soup.find_all('div',attrs={'class':'crux-body-copy'})

products=[div.a.string for div in element]

for items in products:
    print(items)

#both products and link

#products={div.a.string:div.a['href'] for div in soup.find_all('div',attrs={'class':'crux-body-copy'})}

#for key,value in products.items():
#    print(key, '------>', value)