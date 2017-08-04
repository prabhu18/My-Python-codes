
def main():
    a=input()
    for i in range(0,a):
        x=raw_input()
        X=x.split()
        A=int(X[0])
        B=int(X[1])
        sum=0
        for i in range(A,B+1):
            sum=sum+MW(i)
        print sum

def MW(i):
    sum=0
    for j in range(1,i/2+1):
        if(i%j==0):
            g=gcd(j,i)

        if(g==j):
            sum=sum+pow(j,i)

    sum=sum+pow(i,i)
    return sum


def gcd(j,i):
    while(j!=i):
        if(j>=i-1):
            j=j-i
        else:
            i=i-j
    return j



if __name__ == '__main__':
    main()


