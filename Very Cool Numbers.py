__author__ = 'pjha'



def main():
    n=input()

    for i in range(0,n):
        count=0
        h=raw_input()
        H=h.split()
        N=int(H[0])
        K=int(H[1])
        result = ''
        for c in range(0,N+1):
            for x in range(8):
                r = c % 2
                c = c//2
                result += str(r)
            result = result[::-1]


            if result.count('101')>= K:
                count=count+1
        print count




if __name__ == '__main__':
    main()