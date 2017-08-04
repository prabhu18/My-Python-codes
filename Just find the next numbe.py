__author__ = 'pjha'

def main():


    s=input()
    for i in range(1,s+1):
        a=input()

        num="{0:b}".format(a)
        while('11' in num):
            a=a+1
            num="{0:b}".format(a)
        print a


if __name__ == '__main__':
    main()