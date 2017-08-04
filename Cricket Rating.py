__author__ = 'pjha'
def main():
    x=input()
    if(x>0):
        a=raw_input()
        A=a.split()
        S=[]
        for i in range(0,x):
            S.append(int(A[i]))

        max_ending_here=0
        max_sum_so_far=0
        for j in range(0,x):
            max_ending_here=max_ending_here+S[j]

            if(max_ending_here<0):
                max_ending_here=0
            if(max_sum_so_far<max_ending_here):
                max_sum_so_far=max_ending_here

        print max_sum_so_far
    if(x==0):
        print 0




if __name__ == '__main__':
    main()