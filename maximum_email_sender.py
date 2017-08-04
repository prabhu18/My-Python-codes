fname = raw_input("Enter file name: ")
fh = open(fname)
count=0
sum=0
a={}
for line in fh:
    if not line.startswith("From ") : continue
    x=line.split()
    z=x[1]
    if z in a.keys():
        a[z]=a[z]+1
    else:
        a[z]=1
    count=count+1

maxval = None
maxkey = None

for key,val in a.items() :

  if val > maxval:
      maxval = val
      maxkey = key

print maxkey, maxval