__author__ = 'pjha'
def main():
    x=input()
    for i in range(0,x):
        a=input()
        A=[]
        for j in range(0,a):
            s=raw_input()
            A.append(s[0])
        count=0
        for a in  A:
            count=count+1
            if(A.count(a)>1):
                print 'NO'
                break;
            if(count==len(A)):
                print 'YES'
                break




if __name__ == '__main__':
    main()