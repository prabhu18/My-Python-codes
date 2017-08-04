__author__ = 'pjha'

def main():


    s=input()
    for i in range(1,s+1):
        x=raw_input()
        X=x.split()
        A=int(X[0])
        B=int(X[1])
        total=0

        for j in range(A,B+1):

            sum=f=factorial(j)
            if(f>=0 and f<=9):
                sum=f
            else:

                while(sum>9):
                    c=0
                    f=sum
                    while(f>0):
                        c=c+f%10
                        f=f/10
                    sum=c
            total=total+sum

        print total


def factorial(i):
    if(i==0):
        return 1
    else:
        return i*factorial(i-1)


if __name__ == '__main__':
    main()









