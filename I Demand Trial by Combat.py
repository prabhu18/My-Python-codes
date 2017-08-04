__author__ = 'pjha'


def main():
    a=input()
    for i in range(0,a):
        x=raw_input()
        X=x.split()
        P=int(X[0])
        H=int(X[1])
        L=[0]*P
        z=raw_input()
        Z=z.split()
        for j in range(0,P):
            L[j]=int(Z[j])

        for k in range(0,H):
            q=0
            for c in L:
                if(q==0  and L[q+1]==1):
                    L[q]=1


                if(q==0  and L[q+1]==0):
                    L[q]=0


                if(q>=1 and q<P-1 and c==0 and L[q+1]==1 and L[q-1]==1 ):
                    L[q]=1

                if(q==P-1 and c==0 and L[q-1]==1):
                    L[q]=1
                else:
                    L[q]=0

                q=q+1
                print L
        print L





if __name__ == '__main__':
    main()