class node(object):
    def __init__(self,key):
        self.data=key
        self.right=None
        self.left=None


def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print root.data
    inorder(root.right)


def print_vertical(root,dic,distance):
    if root is None:
        return

    try:
        dic[distance].append(root.data)
    except:
        dic[distance]=[root.data]

    print_vertical(root.left,dic,distance-1)
    print_vertical(root.right,dic,distance+1)

def root_in_vertical(root):
    if root is None:
        return
    m=dict()
    distance=0
    print_vertical(root,m,distance)

    for key in sorted(m):
        for i in m[key]:
            print i
        print 'next'

root=node(1)
root.left=node(2)
root.left.left=node(4)
root.left.right=node(5)
root.right=node(3)
root.right.right=node(7)
root.right.right.right=node(9)
root.right.left=node(6)
root.right.left.right=node(8)

#print inorder(root)
print root_in_vertical(root)