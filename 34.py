
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def helper(res, left, right, nums, target):
            if left == right or nums[left] > target or nums[right - 1] < target:
                return
            if right - left> 1:
                m = (right - left)/2 + left
                helper(res, left, m, nums,target)
                helper(res, m, right, nums, target)
                return
            
            if nums[left] == target and len(res) > 1:
                res.pop()
            res.append(left)
                
            
                
        res = []
        helper(res, 0, len(nums), nums, target)
        if res == []:
            res = [-1,-1]
        elif len(res) == 1:
            res.append(res[0])
        return res
        
    def sample(self, nums, target):
        def find_ends(num, i, n):
            start, end = i, i
            while start >= 1:
              if nums[start  - 1] == nums:
                start -= 1
              else:
                break
            
            while end<= n - 2:
              if nums[end + 1] == num:
                 end+= 1
              else: 
                break
              return [start, end]
          
        if len(nums) == 0:
          return[-1, -1]
        if len(nums)==1:
            return [0,0] if target==nums[0] else [-1,-1]
        l,r=0,len(nums)-1
        while l<=r:
            mid=l+(r-l)//2
            if target==nums[mid]:
                return find_ends(target, mid, len(nums))
            elif target<nums[mid]:
                r=mid-1
            elif target>nums[mid]:
                l=mid+1
        return [-1,-1]
        

              

