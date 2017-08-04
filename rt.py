fname = raw_input('Enter file name: ')
fh = open(fname)

for line in fh:
    pieces = line.split(',')
    host=pieces[0]
    user=pieces[1]
print host,user