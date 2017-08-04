v=[1,4,8]
n=3
W=10
w=[1,4,8]



m=[[0 for x in range(W+1)] for y in range(n+1)]

for i in range(1,n+1):
    for j in range(0,W+1):
        if w[i-1] > j :
            m[i][j] = m[i-1][j]
        else:
            m[i][j] = max(m[i-1][j], m[i-1][j-w[i-1]] + v[i-1])

print m[n][W]