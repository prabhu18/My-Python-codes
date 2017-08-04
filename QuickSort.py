def partition(x,low,high):
    i=low-1
    pivot=x[high]

    for j in range(low,high):
        if x[j]<=pivot:
            i=i+1
            x[i],x[j]=x[j],x[i]

    x[i+1],x[high]=x[high],x[i+1]
    return i+1



def quic_sort(x,low,high):
    if low<high:
        pi=partition(x,low,high)

        quic_sort(x,low,pi-1)
        quic_sort(x,pi+1,high)


x=[8,7,5,9,10,1]
l=len(x)
quic_sort(x,0,l-1)
for i in range(l):
    print (x[i]),

