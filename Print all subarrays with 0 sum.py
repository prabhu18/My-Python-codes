def print_all_subarray(arr):
    sum=0
    suba=[]
    Hash={}
    for i in range(0,len(arr)):
        sum=sum+arr[i]
        if sum==0:
            suba.append([0,i])


        if sum in Hash.keys():
            for j in Hash[sum]:
                suba.append([j+1,i])

        try:
            Hash[sum].append(i)
        except:
            Hash[sum]=[i]

    for value in suba:
        print 'sub array index from ' ,value[0],value[1]






arr = [6, 3, -1, -3, 4, -2, 2,4, 6, -12, -7]
print_all_subarray(arr)