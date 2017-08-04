import sys

def getRecord(s):
    max_v,min_v=s[0],s[0]
    max_c=0
    min_c=0

    for i in range(1,len(s)):
        if(s[i]<min_v):
            min_v=s[i]
            min_c=min_c+1
        if(s[i]>max_v):
            max_v=s[i]
            max_c=max_c+1

    z=[]
    z.append(max_c)
    z.append(min_c)
    return z



n = input()
s = map(int,raw_input().strip().split(' '))

result = getRecord(s)
print " ".join(map(str, result))
