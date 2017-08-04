# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count=0
sum=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    sum=sum+float(line[21:])
    count=count+1
print 'Average spam confidence:' , float(sum/count)
