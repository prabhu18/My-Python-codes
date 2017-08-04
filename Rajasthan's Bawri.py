_author_='pjha'

def main():
    x=input()
    for i in range(0,x):
        c=raw_input()
        C=c.split()
        Ax=int(C[0])
        Ay=int(C[1])
        Bx=int(C[2])
        By=int(C[3])

        if(Ax>=Ay):
            Amax=Ax
            Asmall=Ay
        else:
            Amax=Ay
            Asmall=Ax

        if(Bx>=By):
            Bmax=Bx
            Bsmall=By
        else:
            Bmax=By
            Bsmall=Bx



	    if(Amax>=Bmax and Asmall>=Bsmall):
		    print 'Possible'
	    else:
		    print 'Not Possible'










if __name__ == '__main__':
    main()