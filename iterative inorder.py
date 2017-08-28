# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.mlist = []

    #  def inorderTraversal(self, root):
    #        if root is None:
    #            return []
    #       self.inorderTraversal(root.left)
    #        self.mlist.append(root.val)
    #        self.inorderTraversal(root.right)
    #        return self.mlist


    def inorderTraversal(self, root):

        if root is None:
            return []
        flag = 0
        stack = []
        current = root
        while (flag == 0):
            if current is not None:
                stack.append(current)
                current = current.left
            else:
                if len(stack) > 0:
                    current = stack.pop()
                    self.mlist.append(current.val)
                    current = current.right
                else:
                    flag = 1

        return self.mlist

























