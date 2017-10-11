parent=[0,0,0,1,1,1,2,2,7]
newRoot=7

def changeRoot(parent, newRoot):
    parent_of_new_root=parent[newRoot]
    parent[newRoot]=newRoot
    i = parent_of_new_root
    current_parent=newRoot


    while (parent[i] != i):
        old_parent = parent[i]
        parent[i]=current_parent
        current_parent=i
        i=old_parent

    parent[i]=current_parent
    print parent

changeRoot(parent,newRoot)