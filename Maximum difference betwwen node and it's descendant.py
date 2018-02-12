import sys

class node:
    def __init__(self,val):
        self.data=val
        self.right=None
        self.left=None

def inorder(root):
    if root:
        inorder(root.left)
        print root.data,
        inorder(root.right)

def maxabsdiff(root):

    if root is None:
        return sys.maxint

    left=maxabsdiff(root.left)
    right=maxabsdiff(root.right)

    maxabsdiff.diff= max(maxabsdiff.diff,root.data-min(left,right))
    return min(min(left,right),root.data)

root=node(6)
root.left=node(3)
root.right=node(8)
root.right.left=node(2)
root.right.right=node(4)
root.right.left.right=node(7)
root.right.left.left=node(1)
inorder(root)
maxabsdiff.diff=-99999
maxabsdiff(root)
print maxabsdiff.diff