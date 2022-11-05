# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == []:
            return None
        pivot = len(nums) / 2
        root = TreeNode(nums[pivot])
        root.left = self.sortedArrayToBST(nums[0:pivot])
        root.right = self.sortedArrayToBST(nums[pivot + 1:])
        return root

    def sample(self, nums):
        total_nums = len(nums)
        if not total_nums:
           return None
        
        mid_node = total_nums // 2
        return TreeNode(
          nums[mid_node],
          self.sortedArrayToBST(nums[:mid_node], self.sortedArrayToBST(nums[mid_node + 1:]))
        )
            
            
        
        
        