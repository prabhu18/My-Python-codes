__author__ = 'pjha'
__author__ = 'pjha'


def main():
    M=input()
    M_list=[]
    raw_string1 = raw_input()
    Z = raw_string1.split()

    for i in range(0,M):
        M_list.append(int(Z[i]))
        i=i+1
    print(M_list)

    N=input()
    value=0
    for j in range(0,N):
        N_list=[]
        raw_string = raw_input()
        l = raw_string.split()
        List_len=l.__len__()
        for k in range(0,List_len):
            N_list.append(int(l[k]))
            k=k+1
        print(N_list)
        count=0
        for i in range(0,M):
            if(N_list.__contains__(M_list[i])):
                count=count+1
            i=i+1
        if(count==M):
            value=value+1
        j=j+1
    print(value)



if __name__ == '__main__':
    main()
