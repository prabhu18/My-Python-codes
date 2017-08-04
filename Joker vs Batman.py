__author__ = 'pjha'


def main():
    h=input()
    for i in range(0,h):
        A=map(int,raw_input().split())
        N=A[0]
        x=A[1]
        M=A[2]
        z=0
        y=0
        if(x==1 and N==1):
            distance=2
        if(x==1 and N!=1):
            distance=0
        if(x>1):
            z=pow(x,N)
            y=z-1
            distance=2*((x*y)/(x-1))



        print (distance%M)




if __name__ == '__main__':
    main()
