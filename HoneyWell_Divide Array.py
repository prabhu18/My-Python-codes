__author__ = 'pjha'
import sys

def main():
    N=input()
    M=raw_input()
    X=M.split()
    P=[]
    for i in range(0,N):
        P.append(int(X[i]))
    D=input()
    L=P
    product = 1
    for i in range(0,D):
        z=input()
        ##P = map(lambda x: x/z, P)
        product=product*z

    P=[j/product for j in P]



    for x in P:
        print x,






if __name__ == '__main__':
    main()