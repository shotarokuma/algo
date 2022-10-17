# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        if not root: 
            return None
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right,p, q)
        if root.val == p.val or root.val == q.val:
            return root
        if l and r:
            return TreeNode(root.val)
        if l:
            return l
        if r:
            return r
        return None
    
    def sample(self, root,p, q):
        if root is None:
          return None
        if root == p or root == q:
          return root
        left = self.sample(root.left, p, q)
        right = self.sample(root.right, p, q)
        if left and right:
          return root
        return left if left is not None else right