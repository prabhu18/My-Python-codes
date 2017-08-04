__author__ = 'pjha'
import sys

def main():
    N=input()

    for i in range(0,N):
        Ax=raw_input()
        A=Ax.split()
        A1=int(A[0])
        A2=int(A[1])

        if(A1%4==0):
            A1y=3
            A1x=(A1/4)-1
        if(A1%4!=0):
            A1y=(A1%4)-1
            A1x=(A1/4)

        if(A2%4==0):
            A2y=3
            A2x=(A2/4)-1
        if(A2%4!=0):
            A2y=(A2%4)-1
            A2x=(A2/4)

        if( (abs(A1x-A2x)%2==0 and abs(A1y-A2y)%2==0) or (abs(A1x-A2x)%2!=0 and abs(A1y-A2y)%2!=0) ):
            print max(abs(A1x-A2x),abs(A1y-A2y))

        else:
            print 'No'





if __name__ == '__main__':
    main()