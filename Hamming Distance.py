__author__ = 'pjha'
def hamdist(str1, str2):
    diffs = 0
    if(str1.__len__()==str2.__len__()):
        print -1
    else:
        for ch1, ch2 in zip(str1, str2):

            if ch1 != ch2:
                diffs += 1
        print diffs

x=0
y=input()
while(x<y):
    while True:

        try:
            str1 = raw_input()
            str2 = raw_input()
            hamdist(str1,str2) # next line was found
        except (EOFError):
            break #end
    x=x+1
