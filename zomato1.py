__author__ = 'pjha'
x=raw_input()
y={}
for i in range(0,len(x)):
    if(y.__contains__(x[i])):
        pass
    else:
        y[x[i]]=x.count(x[i])

max_val=max(y.values())
min_chr=9999999

for m,n in y.iteritems():
    if(n==max_val):
        if(ord(m)<min_chr):
            min_chr=ord(m)
        else:
            pass
    else:
        pass

print chr(min_chr),
print max_val
