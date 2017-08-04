__author__ = 'pjha'

def main():
    N=input()
    for j in range(0,N):

        M=raw_input()
        l=M.__len__()
        count=0

        for i in range(1,l):
            if(abs(ord(M[i-1])-ord(M[i])) == abs(ord(M[l-i])-ord(M[l-i-1]))):
                count=count+1


        if(count==l-1):
            print "YES"
        else:
            print "NO"






if __name__ == '__main__':
    main()
