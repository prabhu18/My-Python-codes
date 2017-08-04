__author__ = 'pjha'
import sys

def main():
    N=input()
    C=[0]*123
    for i in range(0,N):
        A=raw_input()
        C=[0]*123
        for x in A:
            C[ord(x)]=C[ord(x)]+1
        p=max(C)
        for y in C:
            if(y==p):
                q=C.index(y)
                C[q]=0
                sys.stdout.write(unichr(q))

        print '',
        print p






if __name__ == '__main__':
    main()