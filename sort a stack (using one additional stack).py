def newstack():
    stack=[]
    return stack

def push(stack,data):
    stack.append(data)
def pop(stack):
    if len(stack)>0:
        return stack.pop()

def reverse(z,x):
    ztop=z.pop()
    push(x,ztop)
    xmin=ztop

    while(len(z)>0):
        ztop=z.pop()

        while(xmin<ztop and len(x)>0):
            temp=x.pop()
            push(z,temp)
        push(x,ztop)
        xmin=ztop

    while(len(x)>0):
        print x.pop()


z=newstack()
push(z,1)
push(z,3)
push(z,8)
push(z,12)
push(z,10)
push(z,7)
x=newstack()
reverse(z,x)