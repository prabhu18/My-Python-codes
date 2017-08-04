def check_k_distance(distance,z):
    dict=set()
    for i in range(0,len(z)):



        if z[i] in dict:
            return True

        dict.add(z[i])

        if(i>=distance):
            dict.remove(z[i-distance])

    print dict
    return False


Number_of_elements= input()
z=[]

for i in range(0,Number_of_elements):
    z.append(input())

distance=input()

if check_k_distance(distance,z) :
    print 'Yes'
else:
    print 'No'

