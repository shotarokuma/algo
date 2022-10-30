class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        tail = nums[:len(nums) - k]
        del nums[:len(nums) - k]
        nums.extend(tail)

    def sample(self, nums, k):
        temps = [0] * len(nums)
        for i in range(0, len(nums)):
          temps[(i+k) % len(nums)] = nums[i]
        for i in range(len(nums)):
            nums[i] = temps[i]