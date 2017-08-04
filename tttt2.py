

x=input()
for i in range(0,x):
    y=input()
    d=1
    p=y
    a=[]
    while(p>=1):
        k=p
        count=0
        val=y
        while(val>=0):

            if(val==0):
                a.append(k)
            val=val-p
        p=p-1

    print a

    del a[20000:]






