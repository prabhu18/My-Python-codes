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

def height_of_tree(root):
    if root is None:
        return 0
    else:
        right=height_of_tree(root.right)
        left=height_of_tree(root.left)

        if(right>left):
            return  right+1
        else:
            return  left+1

def print_in_spiral(root,height):

    start=0
    for i in range(1,height+1):
        spiral_print_logic(root,i,start)
        if start == 1:
            start = 0
        else:
            start = 1

def spiral_print_logic(root,depth,start):

    if root is None:
        return

    else:

        if depth == 1 :
            print root.data
        else:

            if start == 0:
                spiral_print_logic(root.right,depth-1,start)
                spiral_print_logic(root.left, depth - 1, start)
            else:
                spiral_print_logic(root.left,depth-1,start)
                spiral_print_logic(root.right, depth - 1, start)

root = node(1)
root.left=node(2)
root.right=node(3)
root.right.left=node(5)
root.right.right=node(4)
root.left.left=node(7)
root.left.right=node(6)

print 'Normal tree'
inorder(root)
print 'Height of tree'
z= height_of_tree(root)
print z
print ''
print_in_spiral(root,z)