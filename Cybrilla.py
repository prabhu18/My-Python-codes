__author__ = 'pjha'

def count_child(l,b):
    count=0
    while(l>0 and b>0):
        if(l!=b):
            if(l>b):
                count=count+1
                l=l-b
                b=b

            if(b>l):
                count=count+1
                b=b-l;
                l=l

        if(l==b):
            count=count+1
            return count


def cadbury(input1,input2,input3,input4):
    count=0
    leng=[]
    while(input1<=input2):
        leng.append(input1)
        input1=input1+1

    bread=[]
    while(input3<=input4):
        bread.append(input3)
        input3=input3+1

    for i in range(0,len(leng)):
        for j in range(0,len(bread)):
            count=count+count_child(leng[i],bread[j])

    return count



cadbury(5,6,3,4)