max_path=[0]*100

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

def print_path(max_path,len):
    for i in range(0,len):
        print max_path[i],
    print ''


def print_all_path_to_leaf(root,max_path,len):

    if root is None:
        return

    else:
        max_path[len]=root.data
        len=len+1

        if root.left is None and root.right is None:
            print_path(max_path,len)
        else:
            print_all_path_to_leaf(root.left,max_path,len)
            print_all_path_to_leaf(root.right,max_path,len)


root = node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)

print 'Normal tree'
inorder(root)
print ''
print_all_path_to_leaf(root,max_path,0)


