_author_='pjha'
import sys
def main():

    s=input()
    for i in range(0,s):
        c=raw_input()
        C=c.split()
        A=[]
        for j in range(0,len(C)):
            A.append(C[j])

        m=0;
        n=len(A)-1;
        while(m<n):
            l=A[m]
            A[m]=A[n]
            A[n]=l
            m=m+1
            n=n-1
        for i in A:
            sys.stdout.write(i)
            sys.stdout.write(" ")
        print
















if __name__ == '__main__':
    main()