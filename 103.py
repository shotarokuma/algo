# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        def helper(root, curr,currLev ,level, zig):
            if not root:
                return
            if currLev == level:
                curr.append(root.val)
                return 
            if zig:
                helper(root.left, curr, currLev + 1, level, zig)
                helper(root.right, curr, currLev + 1, level, zig)
            else:
                helper(root.right, curr, currLev + 1, level, zig)
                helper(root.left, curr, currLev + 1, level, zig)
               
        res = []
        zig = True
        for i in range(2001):
            curr = []
            helper(root, curr, 0, i, zig)
            if curr == []:break
            zig = not zig
            res.append(curr)
        return res
    
    def sample(self, root):
      if not root:return []
      ans,q, c = [], [root],1
      while q:
        n,l = len(q),[]
        for i in range(n):
          curr = q.pop(0)
          l.append(curr.val)
          if curr.left:
            q.append(curr.left)
          if c == 1:
            ans.append(l)
          else:
            ans.append(l[::-1])
          c = 1 -c
      return ans



            
                
            
                
                