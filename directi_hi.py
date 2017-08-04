__author__ = 'pjha'

def final_string(x,y):
    count=0
    for i in range(0,len(x)):
        if(x[i].isdigit()):
            count=count+1
    str=''
    k=0


    for j in range(0,count):
        final=''
        str=''
        k=0

        while(x[k].isdigit()!=True):
            str=str+x[k]
            k=k+1

        if(x[k].isdigit()):
            for m in range(0,int(x[k])):
                final=final+str

        x=final+x[k+1:len(x)]



    print x[y-1]


while(True):
    x=raw_input()
    y=input()
    if(x==False):
        break
    final_string(x,y)
