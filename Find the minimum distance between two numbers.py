
"""
set={3, 5, 4, 2, 6, 3, 0, 0, 5, 4, 8, 3}
"""
z=[]

def minimum_distance(z,x,y):

    distance=999999
    for i in range(0,len(z)):
        if(z[i]==x or z[i]==y):
            prev=i
            break
    for j in range(prev,len(z)):

        if(z[j]== x or z[j]==y):

            if(z[j]== z[prev]):
                prev=j
            else:
                if(abs(prev-j)<distance):
                    distance=abs(prev-j)
                prev=j
    return distance


for i in range(0,input()):
    z.append(input())
x=input()
y=input()

print minimum_distance(z,x,y)