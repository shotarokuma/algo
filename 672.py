# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root, curr):
            if not root.left and not root.right:
                return float("inf")
            tmp = max(root.left.val, root.right.val)
            if curr != tmp:
                return tmp
            left =  helper(root.left, curr)
            right = helper(root.right, curr)
            return left if left < right else right

        if not root.left and not root.right:
            return -1
        if root.right.val > root.left.val:
            minv = helper(root.left, root.val)
            return minv if minv < root.right.val else root.right.val
        elif root.right.val == root.left.val:
            minl = helper(root.left, root.val)
            minr = helper(root.right, root.val)
            return min(minl, minr) if minl != minr else -1
        else:
            minv = helper(root.right, root.val)
            return minv if minv < root.left.val else root.left.val
        