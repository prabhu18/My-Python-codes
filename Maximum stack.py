stack1=[]
stack2=[]

for i in range(input()):
    key=map(int,raw_input().split())
    z=key[0]

    if z == 1:
        val=key[1]

    if z==1:

        stack1.append(val)

        if len(stack2)==0:
            stack2.append(val)
        else:
            top=stack2.pop()
            if val<top:
                stack2.append(top)
                pass
            else:
                stack2.append(top)
                stack2.append(val)

    if z==2:
        k=stack1.pop()
        m=stack2.pop()

        if k==m:
            pass
        else:
            stack2.append(m)

    if z==3:
        maxi=stack2.pop()
        stack2.append(maxi)
        print maxi


