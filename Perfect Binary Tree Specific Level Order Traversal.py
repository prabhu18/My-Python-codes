class newNode:
    def __init__(self,data):
        self.key=data
        self.right=None
        self.left=None


def inorder(root):
    if root is not None:
        inorder(root.left)
        print root.key
        inorder(root.right)

def height(root):
    if root is None:
        return 0
    rheight=0
    lheight=0

    if root.right is not None:
        rheight=height(root.right)
    if root.left is not None:
        lheight=height(root.left)

    if rheight>lheight:
        return rheight+1
    else:
        return lheight+1

def print_specific_binary_tree(root):
    if root is None:
        return

    print root.key,

    if root.left is None:
        return

    print root.left.key,root.right.key,
    queue=[]
    queue.append(root.left)
    queue.append(root.right)

    while(len(queue)>0 and height(root)>=3):
        first=queue.pop(0)
        second=queue.pop(0)

        print first.left.key,second.right.key,
        print first.right.key,second.left.key,
        if first.left.left is not None:
            queue.append(first.left)
            queue.append(second.right)
            queue.append(first.right)
            queue.append(second.left)




root=newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
root.right.left = newNode(6)
root.right.right = newNode(7)
root.left.left.left = newNode(8)
root.left.left.right = newNode(9)
root.left.right.left = newNode(10)
root.left.right.right = newNode(11)
root.right.left.left = newNode(12)
root.right.left.right = newNode(13)
root.right.right.left = newNode(14)
root.right.right.right = newNode(15)
#inorder(root)
#print height(root)
print_specific_binary_tree(root)