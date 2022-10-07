# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def helper(root):
            if root == None:
                return
            helper(root.left)
            helper(root.right)
            tmp = root.right
            root.right = root.left
            tmpR = root
            while tmpR.right != None: 
                tmpR = tmpR.right
            tmpR.right = tmp
            root.left = None
                
        
        helper(root)
        
    def sample(self,root):
      arr = []
      def helper(node):
        if not node:
          return
        arr.append(node)
        helper(node.left)
        helper(node.right)

      helper(root)

      dummy = TreeNode()
      curr = dummy
      for node in arr:
        node.left = None
        node.right = None
        curr.right = node
        curr = curr.right
      
      return dummy.right

        