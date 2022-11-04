class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        def helper(nums, target, start, end):
            if start == end and nums[start] == target:
                return start + 1
            if start == end:
                return 0
            if nums[start] < nums[end] and (target < nums[start] or nums[end] < target):
                return 0
            pivot = (start + end)/2
            return helper(nums, target, start, pivot) + helper(nums, target, pivot + 1, end)
        
        return helper(nums, target, 0, len(nums) - 1) - 1

    def sample(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            return -1