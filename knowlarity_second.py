__author__ = 'pjha'
count=[]
def count_path(z,x,i,j):
    if(i==x[0]-1 and j==x[1]-1):
        count.append(1)
        return

    if(i>= x[0] or j>=x[1]):
        return

    if(z[i][j]==1):
        count_path(z,x,i,j+1)

    if(z[i][j]==2):
        count_path(z,x,i+1,j)


    if(z[i][j]==3):
        count_path(z,x,i+1,j+1)

    if(z[i][j]==4):
        count_path(z,x,i+1,j)
        count_path(z,x,i,j+1)


    if(z[i][j]==5):
        count_path(z,x,i+1,j+1)
        count_path(z,x,i,j+1)

    if(z[i][j]==6):
        count_path(z,x,i+1,j+1)
        count_path(z,x,i+1,j)


    if(z[i][j]==7):
        count_path(z,x,i+1,j+1)
        count_path(z,x,i,j+1)
        count_path(z,x,i+1,j)

    if(z[i][j] in (8,0)):
        ''

    print count
    return len(count)




def no_of_path(input1,input2):
    x=input1
    y=input2
    z=[]
    for k in range(0,x[0]):
        z.append([0]*x[1])

    count=1
    j=0
    k=0
    for i in range(0,x[0]):
        count=1
        j=0
        while(count<=x[1]):
            z[i][j]=y[k]
            j=j+1
            count=count+1
            k=k+1
    print z

    l= count_path(z,x,0,0)
    print l

#input1=[4,6]
#input2=[1,3,0,0,0,0,0,0,4,7,1,0,0,0,0,7,7,6,0,0,0,0,5,0]
input1=[3,3]
#input2=[7,1,0,7,7,6,0,5,0]
input2=[5,1,0,6,7,6,0,5,0]
no_of_path(input1,input2)