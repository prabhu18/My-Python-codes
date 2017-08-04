v=[12,7,5,18]
n=4
W=20
w=[12,7,5,18]



m=[[0 for x in range(W)] for y in range(n)]

for i in range(1,n):
    for j in range(0,W):
        if w[i-1] > j :
            m[i][j] = m[i-1][j]
        else:
            m[i][j] = max(m[i-1][j], m[i-1][j-w[i-1]] + v[i-1])

print m[n-1][W-1]