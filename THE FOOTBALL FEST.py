__author__ = 'pjha'

def main():
    N=input()

    for i in range(0,N):
        a=map(int,raw_input().split())
        Num=a[0]
        Ini=a[1]
        back=Ini
        for j in range(0,Num):
            b=map(str,raw_input().split())

            if(len(b)==2):
                Action=b[0]
                Id=int(b[1])

                
                pos=Id
                back=Ini

            if(len(b)==1):
                pos=back
                back=Ini

            Ini=pos

        print 'Player '+str(pos)











if __name__ == '__main__':
    main()