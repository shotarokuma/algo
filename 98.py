# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root, -float("inf"), float("inf"))
    
    def helper(self, root, minVal, maxVal):
         if not root or (not root.left and not root.right):
            return True
         if root.left and (root.val <= root.left.val or root.left.val <= minVal):
            return False
         if root.right and (root.val >= root.right.val or root.right.val >= maxVal):
            return False
        
         return self.helper(root.left, minVal, root.val) and self.helper(root.right, root.val, maxVal)

    def sample(self, root):
      def valid(node, left, right):
        if not node:
          return True
        elif left >=node.val or right <= node.val:
          return False
        return valid(node.left,left,node.val) and valid(node.right, node.val, right)
      
      return valid(root, float("-inf"), float("inf"))
    