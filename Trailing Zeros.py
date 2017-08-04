
def main():
    x=input()
    for i in range(0,x):

        a=input()
        product=1
        for i in range(1,a+1):
            product=product*i
        count=0
        while(product%10==0):
            count=count+1
            product=product/10
        print count





if __name__ == '__main__':
    main()