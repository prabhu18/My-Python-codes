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

def find_path(root,path,n):
    if(root==None):
        return False
    path.append(root.data)
    if (root.data == n):
        return True

    if ( (root.left and find_path(root.left, path, n)) or
    (root.right and find_path(root.right, path, n)) ):
        return True

    path.pop()
    return False

def lowest_common_ancestor(root,n1,n2):
    n1_path=[]
    n2_path=[]
    if(find_path(root,n1_path,n1)==0 or find_path(root,n2_path,n2)==0):
        return  -1
    if(n1_path.__len__()>n2_path.__len__()):
        x=n2_path.__len__()
    else:
        x=n1_path.__len__()
    i=0
    print n1_path
    print n2_path
    for i in range(0,x):
        if (n1_path[i] != n2_path[i]):
            break
    return n1_path[i-1];


def main():
    root = Tree(1)
    root.left = Tree(2)
    root.right = Tree(3)
    root.left.left = Tree(4)
    root.left.right = Tree(5)
    root.right.left = Tree(6)
    root.right.right = Tree(7)
    print lowest_common_ancestor(root,5,4)











if __name__ == '__main__':
    main()