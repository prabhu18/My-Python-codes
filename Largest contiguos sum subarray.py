input_set=[-2,-3,4,-1,-2,1,5,3]

max_so_far=-999999
max_ending_here=0

for i in range(0,len(input_set)):
    max_ending_here=max_ending_here+input_set[i]

    if max_ending_here < 0:
        max_ending_here=0
    else:
        if max_so_far < max_ending_here:
            max_so_far=max_ending_here

print max_so_far