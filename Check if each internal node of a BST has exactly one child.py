def isbsthasonlyonechild(pre,min,max):
    z=len(pre)-3

    while(z>=0):

        if max<pre[z]:
            max=pre[z]
        else:
            if min>pre[z]:
                min=pre[z]
            else:
                return False
        z=z-1

    return True


pre=[20, 10, 11, 13, 12]
if pre[len(pre)-1]>pre[len(pre)-2]:
    max=pre[len(pre)-1]
    min=pre[len(pre)-2]
else:
    min=pre[len(pre)-1]
    max=pre[len(pre)-2]

print isbsthasonlyonechild(pre,min,max)
