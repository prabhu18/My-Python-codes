"""

Let us create following BST

              50
           /     \
          30      70
         /  \    /  \
       20   40  60   80


Delete 30

"""

class node:
    def __init__(self,data):
        self.key=data
        self.right=None
        self.left=None

def insert(root,data):
    if root is None:
        return node(data)

    if root is not None:
        if root.key>data:
            if root.left is None:
                root.left=node(data)
            else:
                root.left=insert(root.left,data)

        if root.key < data:
            if root.right is None:
                root.right = node(data)
            else:
                root.right = insert(root.right, data)

    return root

def inorder(root):
    if root is not None:
        inorder(root.left)
        print root.key
        inorder(root.right)
    else:
        return

def getminimumnode(root):
    temp=root

    while(temp.left is not None):
        temp=temp.left
    return temp

def deletenode(root,data):
    if root is None:
        return root

    if root.key > data:
        root.left=deletenode(root.left,data)

    else:
        if root.key<data:
            root.right=deletenode(root.right,data)
        else:

            if root.left is None:
                temp=root.right
                root =None
                return temp
            else:
                if root.right is None:
                    temp=root.left
                    root=None
                    return temp
            temp=getminimumnode(root.right)
            root.key=temp.key
            root.right=deletenode(root.right,temp.key)

    return root


root=None
root=insert(root,50)
root=insert(root,20)
root=insert(root,30)
root=insert(root,40)
root=insert(root,60)
root=insert(root,70)
root=insert(root,80)
inorder(root)
root=deletenode(root,30)
print ''
inorder(root)