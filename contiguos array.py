import sys

a=[0,1,1]
n=len(a)

max_len=-sys.maxint
count=0
dict={}
dict[0]=0

for i in range(0,n):

    if a[i]==1:
        count=count+1
    else:
        count=count-1
    try:
        if dict[count] is not None:
            max_len=max(max_len,i+1-dict[count])
    except:
        dict[count]=i+1

print max_len,dict




