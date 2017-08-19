# Driver program to test above function
# key = 65  Key to be searched in BST

""" Let us create following BST
              50
           /     \
          30      70
         /  \    /  \
       20   40  60   80
"""

class node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None



def insert(root,data):
    if root is None:
        return root

    if root.data>data:
        if root.left is None:
            root.left=node(data)
        else:
            root.left=insert(root.left,data)
    else:
        if root.right is None:
            root.right=node(data)
        else:
            root.right=insert(root.right,data)

    return root


def inorder(root):
    if root is not None:
        inorder(root.left)
        print root.data
        inorder(root.right)

def addvalue(root):

    if root is not None:
        addvalue(root.right)
        addvalue.sum=addvalue.sum+root.data
        root.data=addvalue.sum
        addvalue(root.left)
    else:
        return 0




root=node(50)
insert(root,20)
insert(root,30)
insert(root,40)
insert(root,60)
insert(root,70)
insert(root,80)
inorder(root)
addvalue.sum=0
addvalue(root)
print ''
inorder(root)