__author__ = 'pjha'


def main():
    x=input()
    for i in range(0,x):
        count=0
        a=raw_input()
        X=a.split()
        A=int(X[0])
        B=int(X[1])
        for j in range(A,B+1):
            if(palindrome(j)==1):
                count=count+1
        print count

def palindrome(i):
    c=d=str(i)

    if(c==d[::-1]):
        return 1
    else:
        return 0







if __name__ == '__main__':
    main()