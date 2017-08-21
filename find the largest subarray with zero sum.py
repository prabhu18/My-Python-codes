def largest_subarray(a):
    Hash={}
    curr_sum=0
    max_len=0
    for i in range(0,len(a)):
        curr_sum=curr_sum+a[i]

        if a[i]==0 and max_len==0:
            max_len=1

        if curr_sum==0:
            max_len=i+1

        if curr_sum in Hash.keys():
            max_len=max(max_len,i-Hash[curr_sum])
        else:
            Hash[curr_sum]=i


    return max_len


a=[15, -2, 2, -8, 1, 7, 10, 23]
print largest_subarray(a)