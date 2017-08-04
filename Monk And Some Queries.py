__author__ = 'pjha'

def main():
    N=input()
    A=[]
    for i in range(0,N):
        X=raw_input()
        Y=X.split()
        Q1=int(Y[0])
        if Q1 in (1,2):
            Q2=int(Y[1])

        if Q1==1:
            A.append(Q2)

        if Q1==2:
            try:
                C=A.index(Q2)
                del A[C]
            except:
                print -1



        if Q1==3:

            if max(A)=="":
                print -1
            else:
                print max(A)

        if Q1==4:
            if min(A)=="":
                print -1
            else:
                print min(A)


if __name__ == '__main__':
    main()