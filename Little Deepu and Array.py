_author_='pjha'

def main():

    x=input()
    a=raw_input()
    A=a.split()
    C=[]
    for i in range(0,x):
        C.append(int(A[i]))
    p=input()
    for i in range(0,p):
        c=input()
        for j in range(0,x):

            if(C[j]>c):
                C[j]=C[j]-1
    for j in C:
        print j,













if __name__ == '__main__':
    main()