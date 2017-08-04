__author__ = 'pjha'


def main():
    N=input()
    M=raw_input()
    M1=M.split()
    A=[]
    for i in range(0,N):
        A.append(int(M1[i]))
    odd=[]
    even=[]
    for x in A:
        if(int(x)%2==0):
            even.append(int(x))
        else:
            odd.append((int(x)))

    even.sort()
    for x in even:
        print x,
    print sum(even),

    odd.sort()
    for x in odd:
        print x,
    print sum(odd)

if __name__ == '__main__':
    main()