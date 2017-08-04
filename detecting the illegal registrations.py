def main():
    n=input()
    X=[]
    Y=[]
    for i in range(0,n):
        x=raw_input()
        X.append(x)
    c=0
    for y in X:

        if(Y.__contains__(y)):
            X.remove(y)
        else:
            if(X.count(y)>1):
                c=c+1
                Y.append(y)



    print c
    Y.sort()
    for i in Y:

        print i
















if __name__ == '__main__':
    main()