__author__ = 'pjha'
import sys

def main():
    N=input()
    for i in range(0,N):
        x=input()
        Cpre0=0
        Cpre1=1

        for j in range(0,x):
            C0=Cpre1+Cpre0
            C1=Cpre0

            Cpre0=C0
            Cpre1=C1
        print C1,
        print C0,
        print



if __name__ == '__main__':
    main()