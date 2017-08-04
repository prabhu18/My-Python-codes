import sys
import operator

def constructTree(input1):
    x=input1
    y=sorted(list(x))
    z={}
    for i in y:
        if(i in z):
            z[i]=z[i]+1
        else:
            z[i]=1
    #print z

    a=[v[0] for v in sorted(z.iteritems(), key=lambda(k, v): (-v, k))]
    #print a
    k={}
    j=0
    sum=0
    prev=''
    for i in a:
        if(j==0):
            k[i]=0
            j=j+1
            prev=i
        else:
            if(j==len(a)-1):
                k[i]=k[prev]+1
            else:

                k[i]=k[prev]+pow(10,j)
                j=j+1
                prev=i
    s=''
    for j in x:
        s=s+str(k[j])

    return s




input1='acdabebaae'
print constructTree(input1)
