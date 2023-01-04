class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = sorted(nums)
        for i in range(0, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False

    def sample(self, nums):
        res=Counter(nums)
        
        for i in res:
            if res[i]>1:
                return True
        return False