__author__ = 'pjha'

def main():


    s=input()
    for i in range(0,s):
        a=raw_input()
        l=len(a)

        while(a.__contains__('01') ):
            try:

                k=a.index('01')
                if(k):
                    l=len(a)
                    a=a[0:l-1-k]+a[k+2:l-1-k]
            except:

                    c=0


        while( a.__contains__('10')):
            try:
                l=len(a)
                k=a.index('10')

                if(k):
                    l=len(a)

                    a=a[0:l-2-k]+a[k+1:l-2-k]
                    print len(a)
            except:

                    c=0


        print a











if __name__ == '__main__':
    main()






