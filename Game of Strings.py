__author__ = 'pjha'
import re
def main():
    t=input()
    for i in range(0,t):
        x=raw_input()
        X=x.split()
        S=X[0]
        K=int(X[1])
        A=list(S)
        C=list(S)
        C.reverse()

        p=0
        for j in range(0,len(A)):
            if(A[j]==A[0]):
                p=j

        Sub=''.join(A[p:])

        f=A[len(Sub):K]
        st=''.join(f)
        if(st.__contains__(Sub)):
            print Sub;
        else:
            print 'Puchi is a cheat!'



if __name__ == '__main__':
    main()
