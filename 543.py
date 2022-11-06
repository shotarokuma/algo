# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        dp = []
        
        def helper(root, dp):
            if not root:
                return 0
            if not root.left and not root.right:
                dp.append(0)
                return 1
            left = helper(root.left, dp)
            right = helper(root.right, dp)
            dp.append(left + right)
            return left + 1 if left > right else right + 1
        helper(root, dp) 
        return max(dp)

    def sample(self, root):
        if root == None: return True
        l = self.height(root.left)
        r = self.height(root.right)
        return self.dia
    
    def height(self, root):
        if root == None: return 0
        l = self.height(root.left)
        r = self.height(root.right)
        if l + r > self.dia:
          self.dia = l + r
        return max(l, r) + 1
             
            