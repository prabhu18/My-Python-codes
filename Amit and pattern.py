__author__ = 'pjha'


def main():
    N=input()
    # Create a list.
    elements = []

    # Append empty lists in first two indexes.
    for i in range(0,N):
        elements.append([])

    for i in range(0,N):
        for j in range(0,N):
            elements[i].append(input())

    for k in range(0,N):   #RoW
        print elements[k][0],
        print "",
        i=k-1
        j=1
        while(is_valid(i,j,N,N)):
            print elements[i][j],
            print "",
            i=i-1
            j=j+1
    print







def is_valid(i,j,R,C):

    if (i < 0 or i >= R or j >= C or j < 0):
        return False
    else:
        return True




if __name__ == '__main__':
    main()