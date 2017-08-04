__author__ = 'pjha'


def main():
    a=input()
    for i in range(0,a):
        A=raw_input()
        A1=A.split()
        N=int(A1[0])
        M=int(A1[1])
        D=int(A1[2])

        N_Ax=[]
        N_Ay=[]
        for i in range(0,N):
            Z=raw_input()
            Z1=Z.split()
            N_Ax.append(int(Z1[0]))
            N_Ay.append(int(Z1[1]))

        M_Ax=[]
        M_Ay=[]
        for i in range(0,M):
            Z=raw_input()
            Z1=Z.split()
            M_Ax.append(int(Z1[0]))
            M_Ay.append(int(Z1[1]))

        for i in range(0,N):
            count=0
            for j in range(0,M):
                if( abs(N_Ax[i]-M_Ax[j])+abs(N_Ay[i]-M_Ay[j])<=D):
                    count=count+1
            if(count>=M/2):
                print 'YES'
                break;


if __name__ == '__main__':
    main()