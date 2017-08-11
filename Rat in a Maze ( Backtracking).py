"""
Maze :
{{1, 0, 0, 0},
{1, 1, 0, 1},
{0, 1, 0, 0},
{1, 1, 1, 1}}


"""

def issafe(x,y,maze,size):
    return x>=0 and y >=0 and x< size and y<size and maze[x][y]!=0


def solution(maze,size):
    for i in range(0,size):
        for j in range(0,size):
            print maze[i][j],
        print ''


def solveMaze(maze,size):
    maze[0][0]= 2
    xmove=[0,1]
    ymove=[1,0]
    x=0
    y=0

    if(util_function(maze,x,y,xmove,ymove,size)):
        solution(maze,size)
    else:
        print 'No Solution  '

def util_function(maze,x,y,xmove,ymove,size):
    if(x*y==(size-1)*(size-1)):
        return True

    for i in range(0,2):
        x=x+xmove[i]
        y=y+ymove[i]

        if(issafe(x,y,maze,size)):
            maze[x][y]=2

            if(util_function(maze,x,y,xmove,ymove,size)):
                return True
            else:
                maze[x][y]=1
        else:
            x=x-xmove[i]
            y=y-ymove[i]

    return False



size=input('Enter the Maze size : ')
maze=z=[[0 for row in range(0,size)] for col in range(0,size)]
for i in range(0,size):
    for j in range(0,size):
        maze[i][j]=input()
for i in range(0,size):
    for j in range(0,size):
        print maze[i][j],
    print''
print ''

solveMaze(maze,size)
