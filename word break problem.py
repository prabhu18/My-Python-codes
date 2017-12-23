l=['this','is','famous','word','break','problem','problems','words']
string='wordsbreakproblems'
dict={}
for i in l:
    dict[i]=1

def word_break_problem(dict,string,out):

    if len(string)==0:
        print out

    for i in range(1,len(string)+1):
        z=string[0:i]
        key=''.join(z)
        try:
            if dict[key]==1 :
                word_break_problem(dict,string[i:],out+' '+key)
        except:
            pass
word_break_problem(dict,string,'')
