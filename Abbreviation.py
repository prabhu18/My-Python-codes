def get_abbrevation(a,b):

    m=len(b)
    n=len(a)

    dp= [[False for i in range(n+1)] for j in range(m+1)]

    dp[0][0]=True
    flag=0


    for i in range(1,n+1):
        if flag==0:
            if a[i-1].isupper() is True:
                break
            else:
                dp[0][i]=True



    for i in range(1,m+1):
        for j in range(1,n+1):
            if a[j-1]== b[i-1] :
                dp[i][j]=dp[i-1][j-1]
            else:

                if a[j-1].lower()==b[i-1].lower():
                    dp[i][j] = dp[i - 1][j - 1] or dp[i][j - 1]
                else:
                    if a[j-1].isupper() is True:
                        dp[i][j]=False
                    else:
                        dp[i][j]=dp[i][j-1]


    return "YES" if dp[i][j] is True else "NO"

for i in range(0,input()):
    a=raw_input()
    b=raw_input()
    print get_abbrevation(a,b)
