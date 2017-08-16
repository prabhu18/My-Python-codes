""""

Input Tree
       A
      / \
     B   C
    / \   \
   D   E   F


Output Tree
       A--->NULL
      / \
     B-->C-->NULL
    / \   \
   D-->E-->F-->NULL


"""




class  node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
        self.rightside=None



def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print root.data,

    if root.rightside:
        print root.rightside.data,
    else:
        print -1,
    print ''
    inorder(root.right)



def connectnodes(root):
    q=[]
    q.append(root)
    q.append(None)

    while( len(q)>0):
        temp=q.pop(0)

        if temp is not None :
            temp.rightside=q[0]

            if temp.left is not None:
                q.append(temp.left)
            if temp.right is not None:
                q.append(temp.right)

        else:
            if len(q) > 0:
                q.append(None)





root =node('A')
root.left=node('B')
root.right=node('C')
root.left.left=node('D')
root.left.right=node('E')
root.right.right=node('F')
connectnodes(root)
inorder(root)