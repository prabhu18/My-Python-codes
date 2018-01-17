import sys

a=[0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]

'''
Recursive method

def longest_decreasing_subsequence(a,length,pre,begin):

    if begin==length:
        return 0

    exclude=longest_decreasing_subsequence(a,length,pre,begin+1)

    include=0

    if pre>a[begin]:
        include=1+longest_decreasing_subsequence(a,length,a[begin],begin+1)

    return max(include,exclude)
    
#pre=sys.maxint
#begin=0
#print longest_decreasing_subsequence(a,len(a),pre,begin)

'''


#Memoization method

def longest_decreasing_subsequence(a,length):
    res=[0]*length
    res[0]=1

    for i in range(1,length):
        for j in range(0,i):

            if a[j]>a[i] and res[j]>res[i]:
                res[i]=res[j]
        res[i]+=1

    return max(res)

print longest_decreasing_subsequence(a,len(a))