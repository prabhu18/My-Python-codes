__author__ = 'pjha'


def main():
    a=input()
    A=[]
    for i in range(0,a):
        A.append(raw_input())

    count=0
    for i in range(0,a):
        for j in range(i+1,a):
            if(len(A[i])==len(A[j])):
                if(A[i][::-1]==A[j]):
                    count=count+1
    print count


if __name__ == '__main__':
    main()