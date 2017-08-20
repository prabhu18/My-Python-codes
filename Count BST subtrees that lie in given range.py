"""

        10
      /    \
    5       50
   /       /  \
 1       40   100
Range: [5, 45]


"""


class node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None


def push(root,data):
    if root is None:
        return node(data)
    if root.data < data:
        if root.right is None:
            root.right=node(data)
        else:
            root.right=push(root.right,data)
    if root.data > data:
        if root.left is None:
            root.left = node(data)
        else:
            root.left = push(root.left, data)

    return root

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print root.data
    inorder(root.right)

def root_in_range(root,min,max):
    return root.data<=max and root.data>=min

"""
def count_bst_in_given_range(root,min,max):

    if root is None:
        return

    if root_in_range(root,min,max):
        count_bst_in_given_range.count = count_bst_in_given_range.count + 1

    count_bst_in_given_range(root.left,min,max)
    count_bst_in_given_range(root.right,min,max)
"""


def count_bst_in_given_range(root,min,max):
    if root is None:
        return 0
    if root_in_range(root,min,max):
        return 1+count_bst_in_given_range(root.left,min,max)+count_bst_in_given_range(root.right,min,max)

    else:
        if root.data<min:
            return count_bst_in_given_range(root.right,min,max)
        else:
            return count_bst_in_given_range(root.left,min,max)



root=node(10)
push(root,5)
push(root,50)
push(root,1)
push(root,40)
push(root,100)
#inorder(root)
max=45
min=5
count_bst_in_given_range.count=0
print count_bst_in_given_range(root,min,max)
#print count_bst_in_given_range.count