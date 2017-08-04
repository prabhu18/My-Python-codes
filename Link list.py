class Node(object):

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

def get_data(self):
    return self.data

def get_next(self):
    return self.next_node

def set_next(self, new_next):
    self.next_node = new_next
    return new_next


def print_node(node):
    while(node!=None):
        print node.data
        node=node.next_node


node=Node(0)
head=node
for i in range(1,input()):
    node=set_next(node,Node(i))
print_node(head)
