def createstack():
    stack=[]
    return stack

def push(stack,x):
    stack.append(x)

def isempty(stack):
    return len(stack)==0

def pop(stack):
    if (isempty(stack)):
        print 'Overflow'
    else:
        return stack.pop()

def next_greater_element(arr):
    stack=createstack()
    element=0
    next=0
    push(stack,arr[0])

    for i in range(1,len(arr) ):

        next=arr[i]
        if isempty(stack) is not True :
            element = pop(stack)
            while(element < next ):
                print  element,next
                if isempty(stack) is True :
                    break;
                element=pop(stack)
            if (element > next):
                push(stack,element)
        push(stack,next)
    while(isempty(stack) is False):
        print pop(stack),-1

arr=[11,13,21,3]
next_greater_element(arr)

