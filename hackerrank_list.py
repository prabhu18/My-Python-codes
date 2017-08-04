__author__ = 'pjha'


def main():
    N=input()
    A=[]
    for i in range(0,N):
        x=raw_input()
        X=x.split()
        O=X[0]
        A=[0]*3
        if(O=='insert'):
            M=int(X[1])
            N=int(X[2])
            if(M>0):
                A[M-1]=N
            else:
                A[0]=N
        if(O=='print'):
            print A
        if(O=='remove'):
            M=int(X[1])
            del M
        if(O=='append'):
            A.append(X[1])
        if(O=='sort'):
            A.sort()
        if(O=='pop'):
            A.pop()
        if(O=='reverse'):
            A.reverse()






if __name__ == '__main__':
    main()