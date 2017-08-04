__author__ = 'pjha'

import heapq
def main():
    N=input()
    X=[]
    M=raw_input()
    B=M.split()
    for j in range(0,N):
        X.append(int(B[j]))
    for k in range(0,N):
        if(k==0):
            print -1
        if(k==1):
            print -1
        if(k>=2):
            for v in range(0,k):
                d=heapq.nlargest(3, X[0:k+1])
            print (d[0]*d[1]*d[2])




if __name__ == '__main__':
    main()
