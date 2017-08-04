__author__ = 'pjha'

def main():
    x=input()
    for j in range(0,x):
        p=input()
        max=0
        max_val=0
        A=[]
        for i in range(0,p):
            a=map(int,raw_input().split())
            Id=a[0]
            res=a[1]

            if(A.__contains__(Id)==0):

                if(res==1):
                    A.append(Id)
                    max=max+1
                    pre=1
                    max_val=(max_val,max)[max>max_val]
                if(res==0):
                    max=0
                    pre=0
            else:
                if(res==0):
                    max=0
        print max_val








if __name__ == '__main__':
    main()