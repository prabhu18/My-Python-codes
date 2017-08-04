__author__ = 'pjha'


import sys

def main():
    test_case=input()

    for i in range(0,test_case):
        num = input()
        if(num>0 and num <=3):
            print(1)
        else:
            if(num%3==0):
                print(num/3)
            else:
                print(num)
        i=i+1


if __name__ == '__main__':
    main()
