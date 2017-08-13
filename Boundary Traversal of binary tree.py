class Node:
    def __init__(self,data):
        self.key=data
        self.right=None
        self.left=None



def inorder(root):
    if root is not None:
        inorder(root.left)
        print root.key
        inorder(root.right)

def leavesTree(root):
    if root is not None:
        leavesTree(root.left)
        if root.left is None and root.right is None:
            print root.key
        leavesTree(root.right)

def boundaryleft(root):

    if root is not None:

        if root.left is not None:
            print root.key
            boundaryleft(root.left)

        elif root.right is not None:
            print root.key
            boundaryleft(root.right)



def boundaryright(root):

    if root is not None:

        if root.right is not None:
            boundaryright(root.right)
            print root.key
        elif root.left is not None:
            boundaryright(root.left)
            print root.key

def Boundary_traversal(root):
    if root is not None:
        print root.key
        boundaryleft(root.left)
        leavesTree(root.left)
        leavesTree(root.right)
        boundaryright(root.right)



root = Node(20)
root.left = Node(8)
#root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left =  Node(10)
root.left.right.left.left =  Node(16)
root.left.right.right = Node(14)
root.right = Node(22)
root.right.right = Node(25)
#inorder(root)
Boundary_traversal(root)