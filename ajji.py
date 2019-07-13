import urllib.request
from bs4 import BeautifulSoup

fhandle = urllib.request.urlopen('https://ajjibakery.netlify.com/')
soup=BeautifulSoup(fhandle,'html.parser')
tags=soup('a')
for tag in tags:
    print(tag.get('href',None))


