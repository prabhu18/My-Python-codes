__author__ = 'pjha'


def main():
    x=raw_input()
    length=len(x)
    print length
    y=input()
    for i in range(0,y):
        set=2
        p=raw_input()
        P=p.split()
        A=int(P[0])-1
        B=int(P[1])-1
        try:
            if(x[A]==x[B]):
                print 'Yes'

            if(x[A]!=x[B]):
                print 'No'

        except:
            if(x[A%length]==x[B%length]):
                print 'Yes'
            else:
                print 'No'






if __name__ == '__main__':
    main()