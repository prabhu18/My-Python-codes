def main():
    n=input()

    for i in range(0,n):
        x=y=input()
        count=0
        sum_even=0
        sum_odd=0

        while(x != 1):

            if(x%2==0):

                sum_even=sum_even+x
                x=x/2

                count=count+1
            else:

                sum_odd=sum_odd+x
                x=3*x+1
                count=count+1

        sum_odd=sum_odd+1
        sum_odd=sum_odd%count
        sum_even=sum_even%count

        if(sum_even>sum_odd):
            print 'Even Rules'
        if(sum_odd>sum_even):
            print 'Odd Rules'
        if(sum_even==sum_odd):
            print 'Tie'





if __name__ == '__main__':
    main()