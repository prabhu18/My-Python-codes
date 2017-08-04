class node(object):
    def __init__(self,data):
        self.right=None
        self.left=None
        self.data=data

def inorder(root):
    if root is None:
        return
    else:
        inorder(root.left)
        print root.data
        inorder(root.right)

def mirror_tree(node):
    if(node is None):
        return
    else:
        mirror_tree(node.right)
        mirror_tree(node.left)
        node.left,node.right=node.right,node.left


root = node(1)
root.left=node(3)
root.right=node(2)
root.right.left=node(5)
root.right.right=node(4)

print 'Normal tree'
inorder(root)
mirror_tree(root)
print  'Mirror Tree'
inorder(root)


