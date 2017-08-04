class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

def inorder(root):
    if root is None:
        return
    else:
        inorder(root.left)
        print root.data
        inorder(root.right)

def height(root):
    if root is None:
        return 0
    else:
        return 1+ max( height(root.left),height(root.right))

def diameter(root):
    if root is None:
        return  0
    lheight=height(root.left)
    rheight = height(root.right)

    ldiameter = diameter(root.left)
    rdiameter = diameter(root.left)

    return max((1+lheight+rheight),ldiameter,rdiameter)


def diameter_optimized(root,height):

    lheight=0
    rheight=0
    ldiameter=0
    rdiameter=0

    if root is None:
        return  0

    ldiameter = diameter_optimized(root.left,height)
    rdiameter = diameter_optimized(root.right,height)

    height=1+max(rheight,lheight)

    return max((1+lheight+rheight),ldiameter,rdiameter)

root=Node(1)
root.left= Node(2)
root.right= Node(3)
root.left.right=Node(5)
root.left.left=Node(4)

inorder(root)
print height(root)
print diameter(root)
print''
print  diameter_optimized(root,1)


