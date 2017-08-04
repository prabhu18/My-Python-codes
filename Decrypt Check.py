__author__ = 'pjha'
def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

def count_all_prime(l):
    count=0
    for j in l:
        if(is_prime(j)):
            count=count+1
    return count


def count_all_even(l):
    count=0
    for j in l:
        if(j%2==0):
            count=count+1
    return count

def decrpyt(x):
    for i in range(0,x):
        A=[]
        B=[]
        z=raw_input()

        for i in z:
            A.append(int(i))
            B.append(i)
        sum=0
        for k in A[0:3]:
            sum=sum+k
        prime_count=count_all_prime(A[5:])
        even_count=count_all_even(A[5:])
        final_num=''.join(B[3:5])


        if(is_prime(sum) and (A.__contains__(0)==False) and (even_count>=prime_count) and ( is_prime(int(final_num))==False and int(final_num)%6==0) ):
            print 'YES'
        else:
            print 'NO'
	        


print 20
print 1111946232
print 1222542236
print 1234567890
print 3456789120
print 3454665786
print 9875877847
print 1288774840
print 1124243444
print 5454354545
print 2343556777
print 1245805995
print 0000000000
print 1112124688
print 1124243447
print 5454354546
print 2343556774
print 1245805993
print 0000000002
print 1112124681



