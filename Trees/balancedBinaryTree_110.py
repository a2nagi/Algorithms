# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def calculate_height(self, root):
        if root == None:
            return 0
        return 1 + max(self.calculate_height(root.left), self.calculate_height(root.right))
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        
        if root.left and root.right:
            left_height = self.calculate_height(root.left)
            right_height = self.calculate_height(root.right)
            if left_height - right_height >= 2 or right_height - left_height >= 2:
                return False
        
        if root.left and root.right == None:
            left_height = self.calculate_height(root.left)
            if left_height > 2:
                return False
            else:
                return True
        
        if root.right and root.left == None:
            right_height = self.calculate_height(root.right)
            if right_height > 2:
                return False
            else:
                return True
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
        
        
