i=map(int,raw_input().split(' '))
people=i[0]
topics=i[1]
array=[]
for i in range(0,people):
    z=raw_input()
    array.append(z)

max_bit=-1
count=0
l=len(array)
for i in range(0,l):
    for j in range(i+1,len(array)):
        z=int(array[i],2)|int(array[j],2)
        bit=bin(z).count("1")
        if max_bit<bit:
            max_bit=bit
            count=1
        else:
            if max_bit==bit:
                count=count+1

print max_bit
print count

