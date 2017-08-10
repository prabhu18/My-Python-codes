class activity:
    def __init__(self,datastart,dataend):
        self.start=datastart
        self.end=dataend


z=[]
for i in range(0,input('Number of inputs : ')):
    activityStart=input()
    activityEnd=input()
    z.append(activity(activityStart,activityEnd))

print ' '
print 'input start end'
for k in range(0,len(z)):
    print z[k].start,z[k].end

z.sort(key=lambda x: x.end, reverse=False)
i=0
print 'output start end'
print z[i].start,z[i].end
for j in range(1,len(z)):
    if(z[i].end<=z[j].start):
        print z[j].start, z[j].end
        i=j
