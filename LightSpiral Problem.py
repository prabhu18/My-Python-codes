__author__ = 'pjha'

class Tree(object):
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None



def inorder_traverse(node):
    if(node!=None):
        inorder_traverse(node.left)
        print node.data
        inorder_traverse(node.right)

def height(node):
    if(node==None):
        return 0
    else:
        rheight=height(node.right)
        lheight=height(node.left)

    if(rheight>=lheight):
        return rheight+1
    else:
        return lheight+1

def get_light_spiral_tree(current_height,node,previous_height,x):

    if(current_height==previous_height):
        print node.data
        return  0
    else:

        if(x[0]==0):
            if(node.right):
                get_light_spiral_tree(current_height,node.right,previous_height+1,x)

            if(node.left ):
                get_light_spiral_tree(current_height,node.left,previous_height+1,x)
        else:
            if(node.left):
                get_light_spiral_tree(current_height,node.left,previous_height+1,x)
            if(node.right):
                get_light_spiral_tree(current_height,node.right,previous_height+1,x)




    return 0

def light_spiral(node):

    h=height(node)
    c=1
    x=[0]
    for i in range(1,h+1):
        if(i%2==0):
            x[0]=0
        else:
            x[0]=1
        get_light_spiral_tree(i,node,c,x)




def main():
    root=Tree(1)
    root.left = Tree(4);
    root.right = Tree(6);
    root.right.right=Tree(8);
    root.right.left = Tree(7);
    root.right.left.right = Tree(9);
    root.left.right = Tree(3);
    root.left.left = Tree(2);
    root.left.left.right = Tree(11);
    root.left.left.right.right = Tree(12);
    print height(root)
    inorder_traverse(root)
    print ' '
    light_spiral(root)




if __name__ == '__main__':
    main()