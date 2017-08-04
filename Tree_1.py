class Tree(object):
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

def insert(root,data):
    if(root==None):
        return Tree(data)

    if(data<root.data):
        root.left=insert(root.left,data)

    if(data>root.data):
        root.right=insert(root.right,data)

    return root

def inorder(node):
    if(node!= None):

        inorder(node.left)
        print node.data
        inorder(node.right)

def main():
    root=Tree(13)
    insert(root,3)
    insert(root,4);
    insert(root,12);
    insert (root,14);
    insert(root,10)
    insert(root,5);
    insert(root,1);
    insert (root,8);

    insert(root,2);
    insert (root,8);
    insert(root,7);
    insert(root,9);
    insert (root,11);

    insert(root,6);
    insert (root,18);
    inorder(root)



if __name__ == '__main__':
    main()