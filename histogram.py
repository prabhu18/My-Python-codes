import numpy

s = import numpy

s = '''0 0 0 0 1 0
0 0 1 0 0 1
0 0 0 0 0 0
1 0 0 0 0 0
0 0 0 0 0 1
0 0 1 0 0 0'''

nrows = len(s)
ncols = len(s[0]+1)/2
skip = 1
area_max = (0, [])
z=[]

a = numpy.fromstring(s, dtype=int, sep=' ').reshape(nrows, ncols)
w = numpy.zeros(dtype=int, shape=a.shape)
h = numpy.zeros(dtype=int, shape=a.shape)
for r in range(nrows):
    for c in range(ncols):
        if a[r][c] == skip:
            continue
        if r == 0:
            h[r][c] = 1
        else:
            h[r][c] = h[r-1][c]+1
        if c == 0:
            w[r][c] = 1
        else:
            w[r][c] = w[r][c-1]+1
        minw = w[r][c]
        for dh in range(h[r][c]):
            minw = min(minw, w[r-dh][c])
            area = (dh+1)*minw
            if area > area_max[0]:
                area_max = (area, [(r-dh, c-minw+1, r, c)])

z.append(area_max[0])
y=(area_max[0]*100)/(nrows*ncols)
z.append(y)
return z
