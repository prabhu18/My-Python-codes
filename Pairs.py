__author__ = 'pjha'

def main():

    X=map(int,raw_input().split())
    N = X[0]
    K=  X[1]

    L=map(int,raw_input().split())
    L.sort()
    count=0
    for i in range(0,N):
        for j in range(i+1,N):
            if(L[j]-L[i]==K):
                count=count+1
    print count











if __name__ == '__main__':
    main()