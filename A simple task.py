__author__ = 'pjha'
def main():


    x=input()
    A=[]
    B=[]
    for i in range(0,x):
        A.append(input());
    print A
    for i in range(2,9999999):

        A[:] = [x % i for x in A]
        S=set(A)
        if(len(S)==1):
            B.append(i)
    print B

if __name__ == '__main__':
    main()
