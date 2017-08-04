
import re
from bs4 import BeautifulSoup
import urllib2

url =   raw_input("Enter Web address: ")           #"http://python-data.dr-chuck.net/known_by_Fikret.html"



def get_data_from_web(web):
    content = urllib2.urlopen(web).read()
    soup = BeautifulSoup(content, "html.parser")
    #print soup.prettify()
    tags = soup('a')
    #print tags
    i=1
    for tag in tags:

            print  tag['href']



j=0
x = get_data_from_web(url)
