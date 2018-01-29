'''
Quick sort using two pivots ,
Idea is to seperate the array in three parts and
sort recursively.
'''

size=input()
a=map(int,raw_input().split(' '))


def partition(a,low,high):

    if a[low]>a[high]:
        a[low],a[high]=a[high],a[low]

    right_pivot=a[high]
    left_pivot=a[low]

    i=low+1
    j=high-1

    k=low+1

    while(k<=j):

        if a[k]<left_pivot:
            a[k],a[i]=a[i],a[k]
            i=i+1

        elif a[k]>=right_pivot:
            while(j>k and a[j]>right_pivot):
                j=j-1
            a[k],a[j]=a[j],a[k]
            j=j-1
            if a[k]<left_pivot:
                a[k], a[i] = a[i], a[k]
                i = i + 1
        k=k+1

    i=i-1
    j=j+1
    a[i], a[low] = a[low], a[i]
    a[j], a[high] = a[high], a[j]

    return (i,j)

def quicksort(a,low,high):

    if low<high:
        (l,r)=partition(a,low,high)
        quicksort(a,low,l-1)
        quicksort(a,l+1,r-1)
        quicksort(a,r+1,high)

quicksort(a,0,size-1)
print a