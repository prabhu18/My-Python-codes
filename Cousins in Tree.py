__author__ = 'pjha'

class Tree(object):
    def __init__(self,data):
        self.right=None
        self.left=None
        self.data=data


def insert(root,data):
    if(root==None):
        return Tree(data)
    if(data<root.data):
        root.left=insert(root.left,data)
    else:
        root.right=insert(root.right,data)
    return root


def inorder(node):
    if(node!= None):
        inorder(node.left)
        print node.data
        inorder(node.right)

def BtLevel(root,node,lev):
    if(root==None):
        return 0
    if(root.data==node):
        return lev

    l=BtLevel(root.left,node,lev+1)
    if(l!=0):
        return l
    else:
        return BtLevel(root.right,node,lev+1)

def is_sibling(root,node1,node2):
    if(root==None):
        return 0

    if(root.left and root.right):

        return ((root.left.data==node1 and root.right.data==node2) or (root.left.data==node2 and root.right.data==node1) or
            is_sibling(root.left,node1,node2) or is_sibling(root.right,node1,node2))

    return 0

def is_cousin(root,node1,node2):
    if(BtLevel(root,node1,1)==BtLevel(root,node2,1) and is_sibling(root,node1,node2) == 0):
        print 'YES'
    else:
        print 'NO'

def main():
    root=Tree(13)
    insert(root,3)
    insert(root,4)
    insert(root,12)
    insert(root,14)
    insert(root,10)
    insert(root,5)
    insert(root,1)
    insert(root,8)
    insert(root,2)
    insert(root,8)
    insert(root,7)
    insert(root,9)
    insert(root,11)
    insert(root,6)
    insert(root,18)

    is_cousin(root,4,18)



if __name__ == '__main__':
    main()