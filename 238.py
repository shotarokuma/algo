class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res, dp1, dp2 = [], [1], [1]
        n = len(nums)
        for i in range(0, n - 1):
            tmp1 = dp1[-1] * nums[i]
            tmp2 = dp2[0] * nums[i * (-1)- 1]
            dp1.append(tmp1)
            dp2.insert(0, tmp2)
        for i in range(0, n):
            res.append(dp1[i] * dp2[i])
        return res
    
    def sample(self, nums):
      p,prod=[1]*len(nums),1
      for i in xrange(1,len(nums)):
            p[i]=p[i-1]*nums[i-1]
            
      for i in reversed(xrange(len(nums)-1)):
            prod=nums[i+1]*prod
            p[i]=p[i]*prod
      return p

            