class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        m = len(nums)
        res = nums[0] + nums[1] + nums[-1]
        for i in range(m - 2):
            j = i + 1
            k = m - 1
            while j < k:
                curr =  nums[i] + nums[j] + nums[k]
                diff = abs(nums[i] + nums[j] + nums[k] - target)
                if abs(res - target) > diff:
                    res = curr
                if diff == 0:
                    return target
                if curr < target:
                    j += 1
                else:
                    k -= 1
        return res
    
    def sample(self, nums,target):
        n = len(nums)
        nums.sort()
        res = float('inf')
        for i in range(n - 2):
          if i != 0 and nums[i] == nums[i - 1]:
            continue
          j, k = i + 1, n - 1
          while j < k:
            add = nums[i] + nums[j] + nums[k]
            if add == target:
              return add
            elif abs(add - target) < abs(res - target):
              res = add
            if add > target:
              k -= 1
            else:
              j += 1
        return res
                
                
        
        
        
        