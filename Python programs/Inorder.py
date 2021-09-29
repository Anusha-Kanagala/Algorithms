# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result_list = []
        return self.inorder(root, result_list)

    def inorder(self, root, result):
        if root is None:
            return result
        if root.left is not None:
            self.inorder(root.left, result)
        if root is not None:
            result.append(root.val)
        if root.right is not None:
            self.inorder(root.right, result)
        return result
