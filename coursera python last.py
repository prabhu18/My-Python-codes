fname = raw_input("Enter file name: ")
fh = open(fname)
count=0
sum=0
a={}
for line in fh:
    if not line.startswith("From ") : continue
    x=line.split()
    z=x[5].split(':')[0]
    if z in a.keys():
        a[z]=a[z]+1
    else:
        a[z]=1
k=[]
for x in a.keys():
    k.append(x)

k.sort()
for j in k:
    print j,'',a[j]