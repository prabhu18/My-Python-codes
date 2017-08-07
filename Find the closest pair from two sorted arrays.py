"""
int ar1[] = {1, 4, 5, 7};
   int ar2[] = {10, 20, 30, 40};
"""

def closest_pair(arr1,arr2,val,arr1L,arr2L):
    distance=99999999
    low=0
    high=arr2L-1
    res1=low
    res2=high
    while(low<arr1L and high>=0):

        if(abs(arr1[low]+arr2[high]-val)<distance):
            distance=abs(arr1[low]+arr2[high])-val
            res1=low
            res2=high

        if arr1[low]+arr2[high]>val:
            high=high-1
        else:
            low=low+1

    print arr1[res1],arr2[res2]



arr1=[]
arr2=[]

for i in range(0,input()):
    arr1.append(input())

for i in range(0,input()):
    arr2.append(input())

val=input()

arr1L=len(arr1)
arr2L=len(arr2)

closest_pair(arr1,arr2,val,arr1L,arr2L)
