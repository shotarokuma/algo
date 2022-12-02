# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        val = max(nums)
        ind = nums.index(val)
        root = TreeNode(val)
        root.left = self.constructMaximumBinaryTree(nums[:ind])
        root.right = self.constructMaximumBinaryTree(nums[ind + 1:])
        return root
    
    def sample(self, nums):
      if not nums:
        return None
      stk = []
      last = None
      for num in nums:
        while stk and stk[-1].val < num:
          last = stk.pop()
        node = TreeNode(num)
        if stk:
          stk[-1].right = node
        if last:
          node.left = last
        stk.append(node)
        last = None
      return stk[0]
        