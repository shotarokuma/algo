class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dp = [float('inf') for _ in nums]
        dp[0] = 0
        for i in range(len(nums) - 1):
            for j in range(1, nums[i] + 1):
                if i + j >= len(nums):
                    break
                if dp[i + j] > dp[i] + 1:
                    dp[i + j] = dp[i] + 1
        return dp[-1]

    def sample(self, nums):
        l = 0
        r = len(nums) - 1
        j = 0
        while r > 0:
          if l + nums[l] >= r:
              r = l
              j += 1
              l = 0
          else:
            l += 1
        return j



