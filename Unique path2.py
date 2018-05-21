import sys

class Solution(object):
    def uniquePathsWithObstacles(self, grid):

        x = len(grid)  # length
        y = len(grid[0])  # breadth

        result = [[-sys.maxint for i in range(y)] for j in range(x)]

        for i in range(0, y):

            if grid[0][i] == 0:
                result[0][i] = 1
            else:
                break

        for i in range(0, x):

            if grid[i][0] == 0:
                result[i][0] = 1
            else:
                break

        for i in range(1, x):
            for j in range(1, y):

                if grid[i][j] != 1:

                    up = result[i - 1][j]
                    left = result[i][j - 1]

                    if up == -sys.maxint and left == -sys.maxint:
                        pass
                    else:
                        if up != -sys.maxint and left != -sys.maxint:
                            result[i][j] = up + left

                        else:
                            result[i][j] = max(up, left)

        if result[-1][-1] != -sys.maxint:
            return result[-1][-1]
        return 0
