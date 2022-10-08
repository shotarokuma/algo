class Solution(object):
     def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        resl =[]
        
        for i in range(len(nums)):
            if i >= 1 and nums[i - 1] == nums[i]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    resl.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j -1] == nums[j] and j < k:
                        j += 1
                elif s > 0:
                    k -= 1
                else:
                    j += 1
            
        return resl
                
                