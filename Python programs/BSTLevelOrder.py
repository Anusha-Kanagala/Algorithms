# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result_list = []
        open_list =[]
        
        
       
        if root is not None:
            result_list.append([root.val])
        else:
            return result_list
        open_list.append(root)
        
        while(open_list):
            root = open_list.pop(0)
            
            wait_list = []
            wait_list_r =[]
            wait_list_l =[]
            
           
            if root.left is not None:
                wait_list_l.append(root.left.val)
                open_list.append(root.left)
                
                
            if wait_list_l is not None:
                wait_list.extend(wait_list_l)
                
            if root.right is not None:
                wait_list_r.append(root.right.val)
                open_list.append(root.right)
                
            if wait_list_r is not None:
                wait_list.extend(wait_list_r)
            if root.left is None and root.right is None:
                ##return result_list
                pass
            else:
                pass
            
                result_list.append(wait_list)
            
                       
        return result_list
    
                
                
            
        
        