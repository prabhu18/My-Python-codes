class node:
    def __init__(self,V):
        self.array=[]
        self.elements=V
        self.next=None

def print_list(head,size):
    while(head is not None):
        for i in range(0,size):
            print head.array[i]
        head=head.next




head=node(3)
second=node(3)
third=node(3)
head.next=second
second.next=third
head.array.append(1)
head.array.append(2)
head.array.append(3)
second.array.append(4)
second.array.append(5)
second.array.append(6)
third.array.append(7)
third.array.append(8)
third.array.append(9)

print_list(head,head.elements)