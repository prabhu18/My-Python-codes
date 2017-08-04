__author__ = 'pjha'
def main():
    x=input()
    for i in range(0,x):
        a=input()
        s=raw_input()
        S=s.split()
        A=[]
        for j in range(0,a):
            A.append(int(S[j]))

        max=0
        val=0
        D={0:0}
        for j in A:
            if(A.count(j)>max):
                D.clear()
                D[j]=A.count(j)
                val=j
                max=A.count(j)
            if(A.count(j)==max):
                D[j]=A.count(j)
                val=j
                max=A.count(j)
        L=[]
        for k in D:
            L.append(k)
        L.sort(reverse=True)
        for i in L:
            print i,
        print








if __name__ == '__main__':
    main()