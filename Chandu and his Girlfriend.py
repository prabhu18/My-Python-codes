
def main():
    test = input()
    for i in range(0,test):
        size = input()
        unsorted=[]
        array_org = raw_input()
        array=array_org.split()

        for j in range(0,size):
            unsorted[j]=array[j]
            j=j+1
        sorted(array,reverse=True)
        print unsorted
        i=i+1


if __name__ == '__main__':
    main()