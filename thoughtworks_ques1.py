import sys

def main():
    num=raw_input()
    len_value = len(num)

    for i in range(0,len_value):
        count=0
        for j in range(i,len_value):
            if(int(num[j])%2==0):
                count=count+1
            j=j+1
        print(count)
        i=i+1


if __name__ == '__main__':
    main()
