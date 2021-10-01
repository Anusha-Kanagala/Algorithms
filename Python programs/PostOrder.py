# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result_list = []
        return self.postOrder(root, result_list)

    def postOrder(self, root, result):
        if root is None:
            return result
        if root.left is not None:
            self.postOrder(root.left, result)
        if root.right is not None:
            self.postOrder(root.right, result)
        if root is not None:
            result.append(root.val)
        return result
