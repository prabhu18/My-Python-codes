import urllib
import xml.etree.ElementTree as ET

count= 0

while True:
    url = raw_input('Enter location: ')

    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    #print data
    tree = ET.fromstring(data)


    results = tree.findall('comments/comment')
    for list in results:
        count=count+ int(list.find('count').text)

    print count
