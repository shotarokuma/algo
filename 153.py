class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]
        pivot = int(l / 2)
        left = self.findMin(nums[:pivot])
        right = self.findMin(nums[pivot:])
        return min(left, right)

    def sample(self, nums):
        l=0
        h=len(nums)-1
        m=(l+h)>>1
        while l<h:
            if nums[m]>=nums[0]:
                l=m+1
            else:
                h=m
            m=(l+h)>>1
        return min(nums[0],nums[l])