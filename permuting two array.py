for i in range(0,input()):
    var=map(int,raw_input().split(' '))
    k=var[1]
    array1=map(int,raw_input().split(' '))
    array2=map(int,raw_input().split(' '))

    array1.sort()
    array2.sort()

    b=len(array1)-1
    a=0
    flag=0
    for i in range(0,len(array1)):

        if array1[a]+array2[b]>=k:
            a=a+1
            b=b-1
            pass
        else:
            flag=1
            break

    if flag ==1:
        print 'NO'
    else:
        print 'YES'