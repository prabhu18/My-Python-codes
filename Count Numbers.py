__author__ = 'pjha'
import re
def main():
    t=raw_input()
    T=t.split()
    K=int(T[0])
    Test=int(T[1])

    Np=map(int,raw_input().split())

    for i in range(0,Test):
        count=0
        Lp=map(int,raw_input().split())
        A=Lp[0]
        B=Lp[1]
        try:
            for j in range(A,B+1):
                for k in Np:
                    if(j%k==0):
                        count=count+1
                        break
        except:
            print 'hi'
        print count;




if __name__ == '__main__':
    main()
