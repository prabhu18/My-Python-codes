# Given : all nodes are distinct ,if one node or both of them are not present , it will display ' Not feasible'


"""
               10
            /    \
           2      3
         /   \   /
       3     7  9
      / \   / \
     4  5  8   1

"""


class node:

    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None


#for track of counts in both side
def countnode(root,a,b):

    count=0
    if root is None:
        return 0

    if root.data== a or root.data==b:
        return 1

    count = countnode(root.left,a,b)+countnode(root.right,a,b)
    return count


def commonancestor(root,a,b):

    if root is None:
        return

    l=countnode(root.left,a,b)
    r=countnode(root.right,a,b)

    if l==r and l>0 :
        print root.data
        return
    else:
        if l>r and l==2:
            commonancestor(root.left,a,b)
        else:
            if r==2:
                commonancestor(root.right,a,b)

            else:
                print 'Not feasible'

root=node(10)
root.right=node(3)
root.right.left=node(9)
root.left=node(2)
root.left.right=node(7)
root.left.left=node(3)
root.left.left.left=node(4)
root.left.left.right=node(5)
root.left.right.left=node(8)
root.left.right.right=node(1)


commonancestor(root,5,8)