# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        def right(root, val):
            if not root:
                return None
            if root.val < val:
                return root
            err = right(root.left, val)
            return err if err else  right(root.right, val)

        def left(root, val):
            if not root:
                return None
            if root.val > val:
                return root
            err = left(root.left, val)
            return err if err else left(root.right, val)
        if not root:
            return
        while True:
            rnode = right(root.right, root.val)
            lnode = left(root.left, root.val)
            if lnode and rnode:
                lnode.val, rnode.val = rnode.val, lnode.val
            elif lnode:
                lnode.val, root.val = root.val, lnode.val
            elif rnode:
                rnode.val, root.val = root.val, rnode.val
            else:
                break
        self.recoverTree(root.left)
        self.recoverTree(root.right)
        
    def __init__(self):
        self.prev = TreeNode(-sys.maxint)
        
    def sample(self, root):
        two = []
        self.dfs(root, two)
        two[0].val, two[1].val = two[1].val, two[0].val

    def dfs(self, node, two):
        if not node:
            return 
        self.dfs(node.left, two)
        
        if not two and self.prev.val > node.val:    
            two.append(self.prev)
            two.append(node)
        elif self.prev.val > node.val:    
            two[1] = node
        self.prev = node
        
        self.dfs(node.right, two)
        return 
        