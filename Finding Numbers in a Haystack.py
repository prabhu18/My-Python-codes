import re
fname = raw_input("Enter file name: ")
fh = open(fname)
count=0

for line in fh:
    x=re.findall('[0-9]+',line)
    for i in x:
        count = count+int(i)
print count
