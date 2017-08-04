import json
import urllib

url =raw_input("Enter Url: ")

input =urllib.urlopen(url).read()
info = json.loads(input)

count = 0;

for item in info['comments']:
    count=count+item['count']

print count

