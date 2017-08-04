# Uses python2

def editDP(str1, str2, m, n):

    p = [[0 for x in range(n + 1)] for x in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):

            if i == 0:
                p[i][j] = j

            elif j == 0:
                p[i][j] = i

            elif str1[i - 1] == str2[j - 1]:
                p[i][j] = p[i - 1][j - 1]


            else:
                p[i][j] = 1 + min(p[i][j - 1],
                                   p[i - 1][j],
                                   p[i - 1][j - 1])


    return p[m][n]
str1 = raw_input()
str2 = raw_input()
print editDP(str1, str2, len(str1), len(str2))