__author__ = 'pjha'
def main():
    x=input()

    y=input()
    S={}
    for i in range(0,y):
        a=raw_input()
        A=a.split()
        I=int(A[0])
        V=int(A[1])
        S[I]=V


    test=input()
    for i in range(0,test):
        b=raw_input()
        B=b.split()
        m=int(B[0])
        n=int(B[1])
        c=m
        count=0
        ex=0

        try:

            while(S[c]!= n):
                c=S[c]
                count=count+1
        except:
            ex=1
            print 'No Connection'

        if(count==0 and ex==0):
            print 'Direct Connection'

        if(count>=1 and ex==0):
            print 'Indirect Connection'














if __name__ == '__main__':
    main()