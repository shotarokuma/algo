# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root, curr, lTree, rTree):
            if not root:
                return 0
            curr += root.val
            left = helper(root.left, curr, lTree.left, rTree.left)
            right = helper(root.right, curr, lTree.right, rTree.right)
            if root.left:
                lsum = max(lTree.left.val , rTree.left.val) + root.left.val
                lTree.val = lsum if lsum > 0 else 0
            if root.right:
                rsum =  max(lTree.right.val, rTree.right.val) + root.right.val
                rTree.val = rsum if rsum > 0 else 0
            return max(left, right)

        def copyTree(root):
            if not root:
                return None
            node = TreeNode()
            node.left = copyTree(root.left)
            node.right = copyTree(root.right)
            return node

        def search(root, lTree, rTree):
            if not root:
                return float('inf') * (-1)
            ms = lTree.val + rTree.val + root.val
            left = search(root.left, lTree.left, rTree.left)
            right = search(root.right, lTree.right, rTree.right)
            return max(ms, max(left, right))

        lTree = copyTree(root)
        rTree = copyTree(root)
        helper(root, 0, lTree, rTree)
        return search(root, lTree, rTree)

    def sample(self, root):
      max_path = -float('inf')
      def gain_from_subtree(node):
            nonlocal max_path

            if not node:
                return 0
            gain_from_left = max(gain_from_subtree(node.left), 0)
            gain_from_right = max(gain_from_subtree(node.right), 0)
            max_path = max(max_path, gain_from_left + gain_from_right + node.val)
            return max(
                gain_from_left + node.val,
                gain_from_right + node.val
            )

      gain_from_subtree(root)
      return max_path


        
