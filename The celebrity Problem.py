"""
{{0, 0, 1, 0},
{0, 0, 1, 0},
{0, 0, 0, 0},
{0, 0, 1, 0}};
"""

def isknows(a,b,list):
    return list[a][b]==1

def celebrity_problem(list):
    length=len(list[0])
    a=0
    b=length-1

    while(a<b):

        if(isknows(a,b,list)):
            a=a+1
        else:
            b=b-1

    for i in range(0,length):
        if i!=a and (isknows(a,i,list) or (isknows(i,b,list) is False) ):
            return -1
    return a




list=[[0,0,1,0],[0,0,1,0],[0,0,0,0],[0,0,1,0]]
z=celebrity_problem(list)
if z== -1:
    print 'None'
else:
    print z