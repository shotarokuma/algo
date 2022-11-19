class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        def helper(i, curr):
            if i >= len(nums):
                res.append(curr)
                return
            helper(i + 1, list(curr))
            curr.append(nums[i])
            helper(i + 1,list(curr))
            
        helper(0, [])
        return res
    
    def sample(self, nums):
        result = []
        def helper(res,list1):
          res.append(res)
          if not list1:
            return
          for j in range(len(list1)):
              helper(res + [list1[j]], list1[j + 1:])
        for i in range(len(nums)):
          helper([nums[i]], nums[i + 1:])
        return result