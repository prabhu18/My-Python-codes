def numberofways(coin_set,sum,len):

    if sum==0:
        return 1

    if sum<0:
        return 0

    if len<0 and sum>0:
        return 0


    return numberofways(coin_set,sum-coin_set[len],len) + numberofways(coin_set,sum,len-1)


coin_set=[1,2,3]
sum=6

print numberofways(coin_set,sum,len(coin_set)-1)

