fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    x=line.split()
    for z in x:
        if z in lst:
            pass
        else:
            lst.append(z)
lst.sort()
print lst