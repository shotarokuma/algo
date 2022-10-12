# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def helper(root, res, depth, curr):
            if not root:
                return 
            
            if depth == curr and res[depth] == 101:
                res[depth] = root.val
                res.append(101)
                return
            elif depth == curr:
                return
            
            helper(root.right, res, depth, curr + 1)
            helper(root.left, res, depth, curr + 1)
        
        
        res = [101]
        depth = 0
        while True:
            helper(root, res, depth, 0)
            if res[depth] == 101:
                break
            depth += 1
            
        res.pop()
        return res
            
        
        
    def sample(self, root):
        if not root:
          return []
        right = self.sample(root.right)
        left = self.sample(root.left)
        return [root.val] + right + left[len(right):]