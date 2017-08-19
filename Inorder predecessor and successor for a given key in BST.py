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


def findsucpre(root,key):
    if root is None:
        return

    if root.data==key:
        if root.left is not None:
            temp =root.left
            while(temp.right):
                temp=temp.right
            findsucpre.pre=temp

        if root.right is not None:
            temp=root.right
            while(temp.left):
                temp=temp.left
            findsucpre.suc=temp

        return

    else:

        if root.data>key:
            findsucpre.suc=root
            findsucpre(root.left,key)
        else:
            findsucpre.pre=root
            findsucpre(root.right,key)




def inorder(root):
    if root is not None:
        inorder(root.left)
        print root.data
        inorder(root.right)

root=node(50)
insert(root,20)
insert(root,30)
insert(root,40)
insert(root,60)
insert(root,70)
insert(root,80)
inorder(root)
findsucpre.pre=None
findsucpre.suc=None
key=90
findsucpre(root,key)

if findsucpre.pre is not None:
    print 'Predecessor is ' , findsucpre.pre.data
else:
    print 'No Predecessor exists'


if findsucpre.suc is not None:
    print 'Successor is ' , findsucpre.suc.data
else:
    print 'No Successor exists'