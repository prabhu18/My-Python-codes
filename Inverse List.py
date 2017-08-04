


def main():
    n=input()

    for i in range(0,n):
        count=[]
        l=0
        size=input()
        h=raw_input()
        H=h.split()

        for c in range(0,size):
            count.append(int(H[c]))
        for i in range(0,size):
            if(i+1!=count[i]):
                l=1

        if(l==0):
            print 'inverse'
        else:
            print 'not inverse'







if __name__ == '__main__':
    main()