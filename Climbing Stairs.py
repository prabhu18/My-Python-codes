__author__ = 'pjha'



def main():

    T=input()
    for i in range(0,T):
        N=input()
        print(countPossibilities(N))



def countPossibilities(N):
    if (N == 1 or N == 2):
        return N;
    else:
        return countPossibilities(N - 1) + countPossibilities(N - 2);



if __name__ == '__main__':
    main()