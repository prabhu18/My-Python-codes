__author__ = 'pjha'


def main():
    x=input()
    for i in range(0,x):
        s=raw_input()
        l=len(s)
        S=list(s)
        if(l%2==0):
            A=S[0:l/2]
            B=S[l/2:l]


            if(A==B):
                print 'YES'
            else:
                print 'NO'


        else:
            A=S[0:l/2]
            B=S[l/2+1:l]

            if(A==B):
                print 'YES'
            else:
                print 'NO'




if __name__ == '__main__':
    main()