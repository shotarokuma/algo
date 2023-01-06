class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def helper(nums, target, curr, i):
            if target == curr:
                return True
            if i >= len(nums):
                return False
            if curr > target:
                return False
            return helper(nums, target, curr + nums[i], i + 1) or helper(nums, target, curr, i + 1) 
        target = sum(nums)
        if target % 2 != 0:
            return False
        return helper(nums, target / 2, 0, 0)
        
    def canPartition(self, nums):
        total_sum = sum(nums)
        if total_sum & 1: return False
        half_sum = total_sum // 2
        dp = [True] + [False]*half_sum
        for num in nums:
            for j in range(half_sum, num-1, -1):
                dp[j] |= dp[j-num]
        return dp[half_sum]