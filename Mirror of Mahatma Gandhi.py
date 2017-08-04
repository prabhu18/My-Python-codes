__author__ = 'pjha'
def main():
    x=input()
    for i in range(0,x):
        c=raw_input()
        C=list(c)
        l=len(C)
        i=0;
        j=l-1;
        f=1
        while(i<=j):

            if(C[i]!=C[j]):
                f=0
                break;
            if( (i==j) and ( int(C[i]) not in (0,1,8))):
                    f=0
                    break;
            i=i+1;
            j=j-1;
        if(f==1):
            print 'YES'
        else:
            print 'NO'


if __name__ == '__main__':
    main()
