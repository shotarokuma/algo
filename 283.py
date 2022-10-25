class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        remove = 0
        ind = 0
        while ind < len(nums):
            if nums[ind] == 0:
                nums.pop(ind)
                remove += 1
            else:
                ind += 1
            
        for i in range(remove):
            nums.append(0)

    def sample(self, nums):
      start = 0
      last = len(nums) - 1
      for i in range(len(nums)):
        if nums[i] != 0:
          nums[start] = nums[i]
          start += 1
          
      while (last >= start):
        nums[last] = 0
        last = last - 1
        
                