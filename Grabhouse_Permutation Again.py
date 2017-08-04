__author__ = 'pjha'


def main():
    N=input()
    for i in range(0,N):
        x=input()
        X=[0]*x
        X[0]=1
        if(x==1):
            print 1
        if(x==3):
            print 3
        if(x==2):
            print 1
        if(x>3):
            for j in range(0,x):
                if(j>=1):
                    X[j]=int(X[j-1])+1
            if(x%2==0):
                sum=0
                for k in range(0,x/2):
                    sum=sum+abs(int(X[x-k-1])-int(X[k]))
            if(x%2!=0):
                sum=0
                for k in range(0,x/2):
                    sum=sum+abs(int(X[x-k-1])-int(X[k]))

            print sum




if __name__ == '__main__':
    main()