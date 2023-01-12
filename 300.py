class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1 for _ in nums]
        for i in range(len(nums)):
            tmp = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    tmp = max(tmp, dp[j])
            dp[i] += tmp
        return max(dp)
      
    def sample(self, nums):
        sub = []
        for x in nums:
            if len(sub) == 0 or sub[-1] < x:
              sub.append(x)
            else:
              idx = bisect_left(sub, x) 
              sub[idx] = x
        return len(sub)