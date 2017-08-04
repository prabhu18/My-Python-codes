def main():
    s=input()
    k=input()
    for i in range(0,k):
        x=raw_input()
        X=x.split()
        A=int(X[0])
        B=int(X[1])

        if(s>A or s>B):
            print 'UPLOAD ANOTHER'
        else:

            if(B==A):
                print 'ACCEPTED'
            else:
                print 'CROP IT'








if __name__ == '__main__':
    main()