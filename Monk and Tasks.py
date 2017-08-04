import operator

def main():
    a=input()
    for i in range(0,a):
        d=input()
        K=[]
        V=[]
        x=raw_input()
        X=x.split()

        for i in range(0,d):
            K.append(int(X[i]))
            V.append(bin(K[i]).count('1'))

        for j in range(0,d):
            l=V.index(max(V))
            print K[l-1],
            del V[l]









if __name__ == '__main__':
    main()