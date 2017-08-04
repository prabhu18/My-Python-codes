__author__ = 'pjha'


def main():
    x=input()
    a=[]
    for i in range(0,x):
        p=raw_input()
        if(i==0):
            a.append(p)
        else:
            for j in range(0,i):
                if(a.__contains__(p[::-1])):
                    print len(p),
                    print p[len(p)/2]
                    break
                else:
                    a.append(p)





if __name__ == '__main__':
    main()