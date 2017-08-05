"""
1) Input:  txt[] = "BACDGABCDA"  pat[] = "ABCD"
   Output:   Found at Index 0
             Found at Index 5
             Found at Index 6
2) Input: txt[] =  "AAABABAA" pat[] = "AABA"
   Output:   Found at Index 0
             Found at Index 1
             Found at Index 4
"""

txt=raw_input()
pat=raw_input()
M=len(pat)
N=len(txt)
countP=[0]*256
countTW=[0]*256


def compare(arr1,arr2):
    for i in range(0,256):
        if arr1[i]!=arr2[i]:
            return False
    return True

for i in range(0,M):
    countP[ord(pat[i])]=countP[ord(pat[i])]+1
    countTW[ord(txt[i])]=countTW[ord(txt[i])]+1

for i in range(len(pat),len(txt)):
    if compare(countP,countTW):
        print 'Found at Index '  ,i-M

    countTW[ord(txt[i])]=countTW[ord(txt[i])]+1
    countTW[ord(txt[i-M])]=countTW[ord(txt[i-M])]-1


if compare(countP,countTW):
    print 'Found at Index ' ,N-M


