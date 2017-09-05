"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""


def levelOrder(root):
    if root is None:
        return None

    queue = []
    queue.append(root)

    while (len(queue) > 0):

        top = queue.pop(0)
        print top.data,
        if top.left is not None:
            queue.append(top.left)
        if top.right is not None:
            queue.append(top.right)


