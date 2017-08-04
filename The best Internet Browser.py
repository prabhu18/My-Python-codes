def main():
    k=input()
    for i in range(0,k):
        a=raw_input()
        l=len(a)
        count=0

        for x in a[4:l-2]:
            if(x not in ('a','e','i','o','u')):
                count=count+1
        count=count+2
        print '%d/%d' % (count,l)













if __name__ == '__main__':
    main()