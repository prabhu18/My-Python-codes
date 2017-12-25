
def get_all_balanced_paranthesis(result,total_length,open_bracket):

    if total_length%2!=0 and open_bracket== 0:
        return

    if total_length==0:
        if open_bracket==0:
            print result
            return

    if open_bracket>total_length:
        return

    get_all_balanced_paranthesis(result+'(',total_length-1,open_bracket+1)

    if open_bracket>0:
        get_all_balanced_paranthesis(result+')',total_length-1,open_bracket-1)


total_length = 6
open_bracket=0
result=''
get_all_balanced_paranthesis(result,total_length,open_bracket)