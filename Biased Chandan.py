
__author__ = 'pjha'

def main():
    N=input()
    M=[]
    for i in range(0,N):
        M.append(input())

    while M.__contains__(0):
        for x in M:
            a=M.index(x)
            if(x==0 and a>0):
                del M[a],M[a-1]

    print sum(M)





if __name__ == '__main__':
    main()