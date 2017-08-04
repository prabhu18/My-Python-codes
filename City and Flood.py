__author__ = 'pjha'


def main():
    N=input()
    X=[0]*N
    l=0
    for i in range(0,N):
        l=l+1
        X[i]=l

    print X
    M=input()
    for i in range(0,M):
        string=raw_input()
        Y=string.split()
        I=int(Y[0])
        J=int(Y[1])
        P=X.index(J)
        del X[P]

    print X.__len__()





if __name__ == '__main__':
    main()