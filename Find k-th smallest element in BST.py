stack=[]

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


def kthelement(root,k):
    if root is None:
        return 0

    stack.append(root)
    while(root.left is not None):
        root=root.left
        stack.append(root)

    root=stack.pop()
    while(root):
        k=k-1
        if(k==0):
            break

        if root.right is not None:
            root=root.right
            while(root):
                stack.append(root)
                root=root.left
        root=stack.pop()
    return root.data



def inorder(root):
    if root is not None:
        inorder(root.left)
        print root.data
        inorder(root.right)

root=node(20)
insert(root,8)
insert(root,22)
insert(root,4)
insert(root,12)
insert(root,10)
insert(root,14)
#inorder(root)
k=2
print kthelement(root,k)