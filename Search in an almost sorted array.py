"""
{3, 2, 10, 4, 40}
"""


l=[]

def look_element_in_array(l,x,low,high):
    if(low>=high):
        return -1
    else:
        mid=(low+high)/2

        if(l[mid]==x):
            return mid
        if(mid>low and l[mid-1]== x):
            return mid-1
        if(mid<high and l[mid+1]==x):
            return mid+1
        if(l[mid]>x):
            return look_element_in_array(l,x,low,mid-2)
        else:
            return look_element_in_array(l,x,mid+2,high)



for i in range(0,input()):
    l.append(input())

look_element=input()
low=0
high=len(l)
print look_element_in_array(l,look_element,low,high)