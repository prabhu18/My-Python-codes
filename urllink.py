

from bs4 import BeautifulSoup
import urllib2

url = "http://www.dr-chuck.com"
content = urllib2.urlopen(url).read()

soup = BeautifulSoup(content,"html.parser")

tags = soup('a')

for tag in tags :
    if tag.has_attr('href'):
        print tag['href']