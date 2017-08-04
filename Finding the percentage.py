__author__ = 'pjha'


def main():
    N=input()
    dict={}
    for i in range(0,N):
        x=raw_input()
        X=x.split()
        key=X[0]
        value=float(X[1])+float(X[2])+float(X[3])
        dict[key]=value

    y=raw_input()
    print("%.2f" % (dict[y]/float(3)))








if __name__ == '__main__':
    main()