__author__ = 'pjha'

def main():
    N=input()
    for j in range(0,N):

        M=raw_input()
        l=M.__len__()
        count=0
        x=1
        track=[0]*123
        for i in range(0,l):
            if(ord(M[i])>=97 and ord(M[i])<=122 and track[i]== 0):
                track[ord(M[i])]=1


        for j in range(97,123):
            if(track[j]==0):
                x=0
        if(x==1):
            print "YES"
        else:
            print "NO"






if __name__ == '__main__':
    main()