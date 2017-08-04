__author__ = 'pjha'

def main():
    N=input()

    for i in range(0,N):
        M=input()
        sum=0
        for j in range(0,M):
            a=map(int,raw_input().split())
            sum=sum+a[1]*a[0]

        while(sum>9):
            fsum=0
            while(sum>0):
                fsum=fsum+sum%10
                sum=sum/10
            sum=fsum
        print sum








if __name__ == '__main__':
    main()