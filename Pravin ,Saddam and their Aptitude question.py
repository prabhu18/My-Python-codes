__author__ = 'pjha'


def main():
    N=input()
    for i in range(0,N):
        x=raw_input()
        X=x.split()
        A=int(X[0])
        B=int(X[1])
        product=0

        for i in range(A,B+1):
            product=product+fact(i)
        print product%10




def fact(i):
    if i==0:
        return 1
    else:
        return fact(i-1)*i




if __name__ == '__main__':
    main()