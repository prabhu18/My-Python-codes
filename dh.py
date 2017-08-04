def calculate_sum(input1,input2):
	x=input1-2
	y=input2-2
	if(input1==0):
		x=0
		sumx=0
	if(input1==1):
		x=1
		sumx=1
	if(input1>=2):
		sumx= (x*(x+1))/2
	
	sumy= (y*(y+1))/2 
	
	return 2*(sumy-sumx)+y+1+x

print calculate_sum(10,19)