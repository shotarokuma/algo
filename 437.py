# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        
        def subhelper(root, targetSum, curr):
            if root == None:
                return 0
            curr += root.val
            if curr == targetSum:
                return subhelper(root.left, targetSum,curr) + subhelper(root.right, targetSum,curr) + 1
            else:
                return subhelper(root.left, targetSum,curr) + subhelper(root.right, targetSum,curr)
        
        def helper(root, targetSum):
            if root == None:
                return 0
            return subhelper(root, targetSum, 0) + helper(root.left,targetSum) + helper(root.right, targetSum)
            
        return helper(root, targetSum)

    def sample(self, root, targetSum):
        def dfs(n , s):
          if not n:
            return 0
          return (n.val == s) + dfs(n.left, s - n.val) + dfs(n.right, s - n.val)
        
        if not root:
          return 0

        return dfs(root, sum) + self.sample(root.left, sum) + self.sample(root.right, sum)