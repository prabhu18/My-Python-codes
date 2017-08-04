__author__ = 'pjha'


def main():
    a=input()
    for i in range(0,a):
        d=raw_input()
        D=d.split()
        N=int(D[0])
        M=int(D[1])
        A=int(D[2])
        B=int(D[3])
        C=int(D[4])


        if(A*N+B*M>=(N+M)*C):
            print A*N+B*M
        else:
            print (M+N)*C


if __name__ == '__main__':
    main()