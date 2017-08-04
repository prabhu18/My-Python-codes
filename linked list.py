class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):

        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def getCount(self, node):
        if (not node):
            return 0
        else:
            return 1 + self.getCount(node.next)

    def print_nodes(self,node):
        while(node!=None):
            print node.data,
            node=node.next
        print ''

    def delete_nodes(self,data):
        node=self.head
        while(node.next.data!=data):
            node=node.next
        node.next=node.next.next

    def create_a_loop(self,data):
        node=self.head
        while(node.data!=data):
            node=node.next
        node.next=self.head.next

    def find_a_circle(self):
        x=self.head
        y=self.head
        s=0
        while(s==0):
            x=x.next
            y=y.next.next

            if(x==y):
                s=1
                print "loop found"
                return
        print "loop not found"

    def reverse_link_list(self):
        pre=None
        curr=self.head
        next=None

        while(curr!=None):
            next=curr.next
            curr.next=pre
            pre=curr
            curr=next
        self.head=pre

    def reverse_link_list_in_group(self,k):
        pre=None
        next=None
        curr=self.head
        count=0
        while(curr!=None and count<k):
            next=curr.next
            curr.next=pre
            pre=curr
            curr=next
            count=count+1

        if(next!=None):
            self.head.next=self.reverse_link_list_in_group(k)

        return pre





if __name__=='__main__':
    llist = LinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(5)
    llist.push(6)
    llist.push(7)
    llist.push(8)
    llist.push(9)
    llist.push(10)
    llist.push(11)
    llist.push(12)
    llist.push(13)
    print 'Count of nodes is :',llist.getCount(llist.head)
    llist.print_nodes(llist.head)
    #llist.delete_nodes(3)
    #llist.print_nodes(llist.head)
   # llist.create_a_loop(4)
   # llist.find_a_circle()
   # llist.reverse_link_list()
   # llist.print_nodes(llist.head)
    llist.reverse_link_list_in_group(3)
    llist.print_nodes(llist.head)

