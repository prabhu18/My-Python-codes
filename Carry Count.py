def main():
    n=input()
    for i in range(0,n):
        x=raw_input()
        X=x.split()
        A=list(X[0])
        B=list(X[1])

        lenA=len(A)
        lenB=len(B)

        if(lenA>lenB):
            loop=lenA
        else:
            loop=lenB

        A.sort(reverse=True)
        B.sort(reverse=True)
        carry=0
        sum=0
        count=0
        for i in range(0,loop):

            try:
                var1=int(A[i])
            except:
                var1=0

            try:
                var2=int(B[i])
            except:
                var2=0

            sum=var1+var2+carry
            if(sum>9):
                if(sum==10):
                    carry=1
                else:
                    carry=sum%10
                count=count+1
        if(count==0):
            print 'No carry operation'
        else:
            if(count==1):
                print '%d' % (count)+ ' carry operation'
            else:
                print '%d' % (count)+ ' carry operations'






if __name__ == '__main__':
    main()