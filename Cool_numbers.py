__author__ = 'pjha'



def main():
    N=input()
    for i in range(0,N):
        X=input()
        product=1
        if(X==0):
            print 1
        if(X==1):
            print 1
        if(X>=2):
            for j in range(1,X+1):
                product=product*j
            print product



if __name__ == '__main__':
    main()