class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList():
    def __init__(self):
        self.head=None

    def printlist(self):
        temp=self.head

        while(temp is not None):
            print temp.data
            temp=temp.next
        print ''

    def push(self,data):

        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode

    def reverse(self,posofnode):

        if posofnode is not None:
            current=posofnode
        else:
            current=self.head

        prev=None


        while(current is not None):
            next=current.next
            current.next=prev
            prev=current
            current=next

        self.head=prev

    def palindrome_check(self):
        if self.head is None or self.head.next is None:
            return 'False'

        temp=self.head
        prev=self.head
        slow=self.head
        fast=self.head
        midnode=None

        while(fast is not None and fast.next is not None):
            fast=fast.next.next
            prev=slow
            slow=slow.next

        if(fast is not None):
            midnode=slow
            slow=slow.next
            midnode.next = None

        prev.next = None
        secondhalf=slow

        self.reverse(secondhalf)
        result=self.comparelist(temp,self.head)


        self.reverse(self.head)
        if midnode is not None:
            prev.next=midnode
            midnode.next=secondhalf
        else:
            prev.next=secondhalf

        self.head=temp
        print result

    def comparelist(self,head1,head2):

        while(head1 is not None and head2 is not None):

            if head1.data==head2.data:
                head1=head1.next
                head2=head2.next

            else:
                return False
        if(head1 is None and head2 is None):
            return  True

        return 0

    def linktwolist(self,llist1):
        listhead2= self.head
        listhead1=llist.head

        while listhead2.next is not None:
            listhead2=listhead2.next
            listhead1=listhead1.next

        listhead2.next=listhead1.next

        self.printlist()



llist = LinkedList()
llist.push(1)
llist.push(4)
llist.push(3)
llist.push(4)
llist.push(1)
llist.printlist()
#llist.reverse(None)
llist.palindrome_check()
llist.printlist()

llist2=LinkedList()
llist2.push(7)
llist2.push(5)

llist2.linktwolist(llist)




"""
palindrome=raw_input()
for i in range(0,len(palindrome)):
    llist.push(palindrome[i])

print llist.palindrome_check()

"""