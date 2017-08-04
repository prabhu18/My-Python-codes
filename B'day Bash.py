__author__ = 'pjha'

def main():
    h=input()
    for i in range(0,h):
        A=map(int,raw_input().split())
        Amount=A[0]
        S=A[1]
        B=A[2]
        F=A[3]
        S_amount=100
        B_amount=50
        F_amount=25

        S_consume=S_amount*S
        B_consume=B_amount*B
        F_consume=F_amount*F

        left_over= Amount - S_amount-B_consume-F_consume
        if(left_over==0):
            print S_consume,
            print B_consume,
            print F_consume
        if(left_over<0):
            print 'No'

        if(left_over>0):
            if(left_over<S_consume):
                if(left_over<B_consume):
                    if(left_over<F_consume):
                        Flag=1
                    






if __name__ == '__main__':
    main()
