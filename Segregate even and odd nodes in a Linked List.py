class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linklist:
    def __init__(self):
        self.head=None

    def printlist(self):
        temp=self.head
        while(temp is not None):
            print  temp.data
            temp=temp.next

    def push(self,data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode

    def segregate_even_odd(self):
        current=self.head
        evenstart=None
        evenend=None
        oddstart=None
        oddend=None


        while(current is not None):

            if(current.data%2==0):

                if(evenstart is None):
                    evenstart=current
                    evenend=evenstart
                else:
                    evenend.next=current
                    evenend=evenend.next

            else:

                if(oddstart is None):
                    oddstart=current
                    oddend=oddstart
                else:
                    oddend.next=current
                    oddend=oddend.next

            current=current.next

        if oddstart is None or evenstart is None :
            return

        evenend.next=oddstart
        oddend.next=None
        self.head=evenstart




list=Linklist()
list.push(11)
list.push(10)
list.push(9)
list.push(6)
list.push(4)
list.push(1)
list.push(0)

list.printlist()
print ''

list.segregate_even_odd()
list.printlist()