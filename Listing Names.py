__author__ = 'pjha'


def main():
    x=input()
    A={}
    for i in range(0,x):
        p=raw_input()

        try:
            if(A[p]):
                A[p]=A[p]+1
        except:
            A[p]=1
    for x in sorted(A):
        print x,
        print A[x]




if __name__ == '__main__':
    main()