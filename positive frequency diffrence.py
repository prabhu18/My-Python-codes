__author__ = 'pjha'


def max_freq_diff(x,y):
    left=[0]*x
    maxium=0
    min_so_far=y[0]
    for i in range(1,x):
        if(y[i]<min_so_far):
            left[i]=maxium
            min_so_far=y[i]
        else:
            maxium=max(maxium,y[i]-min_so_far)
            left[i]=maxium

    print left
    right=[0]*x
    maxium=0
    max_so_far=y[x-1]

    for j in range(x-2,-1):
        if(y[j]>max_so_far):
            right[j]=maxium
            max_so_far=y[j]
        else:
            maxium=max(maxium,max_so_far-y[j])
            right[j]=maxium


    print right
    maxium=0
    for i in range(0,x):
        maxium=max(maxium,left[i]+right[i])

    return maxium






def main():
    x=input()
    y=map(int,raw_input().split())
    print max_freq_diff(x,y)



if __name__ == '__main__':
    main()