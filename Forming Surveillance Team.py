
__author__ = 'pjha'
def main():
    t=input()
    for i in range(0,t):
        n=input()
        a=map(int,raw_input().split())
        s=list(set(a))
        print len(s)



if __name__ == '__main__':
    main()