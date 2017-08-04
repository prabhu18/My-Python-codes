number_of_employee=input()
dict={}
for i in range(0,number_of_employee):
    employee=raw_input()
    dict[employee]=raw_input()

print dict
z=list(set(dict.values()))

new_dict={}

for i in z:
    new_dict[i].set()
    for key,value in dict.items():
        if value==i:
            new_dict[i].add(key)
print new_dict
