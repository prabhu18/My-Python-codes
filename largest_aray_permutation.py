__author__ = 'pjha'


def main():

    N,K  = map(int,raw_input().split())
    A = map(int,raw_input().split())

    I = [0]*(N+1)

    for i in xrange(N): I[A[i]] = i

    print A
    print I
    for i in xrange(N):
        if K==0:
            break
        if A[i]==N-i:
            continue
        A[I[N-i]] = A[i]
        A[i] = N-i
        I[A[I[N-i]]] = I[N-i]
        I[N-i] = i
        K-=1
    print ' '.join(map(str,A))



if __name__ == '__main__':
    main()