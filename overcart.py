__author__ = 'pjha'

def main():


    s=input()
    for i in range(1,s+1):
        a=input()
        count=0
        for j in range(1,a+1):


            if(1<=j>=9):

                count=count+1

            if(10<=j>=99):

                count=count+2

            if(100<=j>=999):

                count=count+3

            if(1000<=j>=9999):

                count=count+4

            if(10000<=j>=99999):

                count=count+5

            if(100000<=j>=999999):


                count=count+5

        		
            if(1000000<=j>=9999999):

                count=count+5

            if(10000000<=j>=99999999):

                count=count+5

            if(100000000<=j>=999999999):

                count=count+5
       
       
        print count;


if __name__ == '__main__':
    main()