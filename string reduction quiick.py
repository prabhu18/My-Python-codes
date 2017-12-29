def stringReduction(a):
    total_a=len(a.replace('b','').replace('c',''))
    total_b=len(a.replace('c','').replace('a',''))
    total_c=len(a.replace('a','').replace('b',''))

    if total_b==0 and total_c == 0 and total_a !=0:
        return total_a

    if total_a == 0 and total_c == 0 and total_b != 0:
        return total_b

    if total_b == 0 and total_a == 0 and total_c != 0:
        return total_c

    if total_a%2==0 and total_b%2==0 and total_c%2==0:
        return 2

    if total_a % 2 != 0 and total_b % 2 != 0 and total_c % 2 != 0:
        return 2

    return 1


t = input()
for i in range(0, t):
    a = raw_input()
    print stringReduction(a)
