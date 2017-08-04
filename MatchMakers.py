__author__ = 'pjha'

def main():
    a=input()
    for i in range(0,a):
        count=0
        d=input()
        girls=[]
        boys=[]
        g=raw_input()
        b=raw_input()

        g_list=g.split()
        b_list=b.split()
        for j in range(0,d):
            girls.append(int(g_list[j]))
            boys.append(int(b_list[j]))



        girls.sort(reverse=False)
        boys.sort(reverse=True)
        print girls
        print boys
        for j in range(0,d):
            if( (girls[j]%boys[j]==0) or (boys[j]%girls[j]==0)):
                count=count+1
        print count





if __name__ == '__main__':
    main()