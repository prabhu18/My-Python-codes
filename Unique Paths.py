class Solution(object):
    def uniquePaths(self, x, y):

        result = [[0 for i in range(y)] for j in range(x)]

        for i in range(0, y):
            result[0][i] = 1

        for i in range(0, x):
            result[i][0] = 1

        for i in range(1, x):
            for j in range(1, y):
                result[i][j] = result[i - 1][j] + result[i][j - 1]

        return result[-1][-1]
