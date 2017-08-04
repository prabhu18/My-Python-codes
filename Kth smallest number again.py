__author__ = 'pjha'


def main():
    N=input()
    for i in range(0,N):
        X=raw_input()
        X1=X.split()
        X2=int(X1[0])
        X3=int(X1[1])
        for j in range(0,X2):
            Y=raw_input()
            Y1=Y.split()
            Y2=int(Y1[0])
            Y3=int(Y1[1])
            C=[0]*(Y3-Y2+1)
            c=0
            for l in range(Y2,Y3+1):
                C[c]=l
                c=c+1
            C.sort(reverse=False)
            for p in range(0,Y3):
                val=input()
                try:
                    print C[val-1]
                except:
                    print-1









if __name__ == '__main__':
    main()