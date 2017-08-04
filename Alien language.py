__author__ = 'pjha'


def main():
    N=input()
    for i in range(0,N):
        A=raw_input()
        B=raw_input()
        if(A.__contains__(B)):
            print 'YES'
        else:
            print 'NO'


if __name__ == '__main__':
    main()