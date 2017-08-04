__author__ = 'pjha'

def main():
    s=input()
    for i in range(0,s):
        d=raw_input()
        l=list(d)
        while(common_char(l)):
            for j in range(0,len(l)-1):
                if(l[j]==l[j+1]):
                    del l[j]
                    break;
        u=''.join(l)
        print u



def common_char(l):
    p=len(l)
    for i in range(0,p-1):
        if(l[i]==l[i+1]):
            return True;
    return False



if __name__ == '__main__':
    main()