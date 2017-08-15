class List:
    def __init__(self, data):
        self.data = data
        self.next = None


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class conversion:
    def __init__(self):
        self.head=None
        self.root=None

    def push(self,data):
        newNode=List(data)
        newNode.next=self.head
        self.head=newNode

    def convertotree(self):

        queue=[]

        if self.head is  None:
            self.root = None
            return

        self.root=Node(self.head.data)
        queue.append(self.root)
        self.head=self.head.next
        while(self.head is not None):
            parent=queue.pop(0)


            leftNode=Node(self.head.data)
            self.head=self.head.next
            parent.left=leftNode
            queue.append(leftNode)

            if self.head is not None:
                rightNode=Node(self.head.data)
                self.head=self.head.next
                parent.right=rightNode
                queue.append(rightNode)

    def inorder(self,root):

        if root is None:
            return
        self.inorder(root.left)
        print root.data
        self.inorder(root.right)

    def printlist(self):
        temp=self.head
        while(temp is not None):
            print temp.data
            temp=temp.next

c = conversion()
c.push(36)
c.push(30)
c.push(25)
c.push(15)
c.push(12)
c.push(10)

#c.printlist()
c.convertotree()
c.inorder(c.root)

