## Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTDepth(object):

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            count = 1
            depth = self.nodeCount(root,count)
            ##return depth
            print(depth)
        else:
            ##return 0
            print(0)

    def nodeCount(self, root,count):

        if root:
            if root.right and not root.left:
                count = count + 1
                return self.nodeCount(root.right,count)
            elif root.left and not root.right:
                count = count + 1
                return self.nodeCount(root.left,count)
            elif root.right and root.left:
                count = max(self.nodeCount(root.right,count), self.nodeCount(root.left,count))
                count = count + 1
            else:
                return count
        return count


def printDepth():
    c5 = TreeNode(5, None, None)
    c4 = TreeNode(4, c5, None)
    c3 = TreeNode(3, c4, None)
    c2 = TreeNode(2, c3, None)
    root = TreeNode(1, c2, None)
    bst = BSTDepth()
    bst.maxDepth(root)


printDepth()
