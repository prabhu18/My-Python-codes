__author__ = 'pjha'


def main():



    for i in range(1,10001):



        if(i%3==0 and i%5!=0):

            print 'Fizz'

        else:
            if(i%5==0 and i%3!=0):

                print 'Buzz'

            else:
                if(i%5==0 and i%3==0):

                    print 'FizzBuzz'
                else:
                    print i




if __name__ == '__main__':
    main()