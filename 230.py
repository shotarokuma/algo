class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def helper(root, k, curr):
            if not root:
                return
            helper(root.left, k , curr)
            if not root.left and not root.right:
                curr.append(root.val)
                return
            while root:
                curr.append(root.val)
                root = root.right
                if root and root.left:
                    helper(root.left,k ,curr)
        
        curr = []
        helper(root, k , curr)
        return curr[k - 1]
    
    def sample(self, root, k):
        def tree_to_list(root):
          if not root:
            return []
          
          return tree_to_list(root.right) + [root.val] + tree_to_list(root.left)
        tree_list = tree_to_list(root)
        return tree_list[-k]
    