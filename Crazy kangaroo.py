def main():
    N=input()
    for i in range(0,N):
        X=raw_input()
        X1=X.split()
        A=int(X1[0])
        B=int(X1[1])
        C=int(X1[2])
        count=0
        while(A<=B):
            if(A%C==0):
                break;
                A=A+C
                count=count+1

            if(count==0):
                A=A+1

        while(A<=B):
            if(B%C==0):
                break;
                A=A+C
                count=count+1

            if(count==0):
                B=B-1


        print ((B-A)/C)+1

if __name__ == '__main__':
    main()