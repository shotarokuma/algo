class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        def helper(nums):
            n = len(nums)
            for i in range(0, n):
                for j in range(i + 1, n):
                    if nums[j] % nums[i] == 0:
                        nj = nums.pop(j)
                        ni = nums.pop(i)
                        return [ni, nj]
            return []
        if len(nums) < 2:
            return nums
        nums = sorted(nums)
        res = helper(nums)
        if res == []:
            return [nums[0]]
        i = 0
        while i < len(nums):
            if nums[i] % res[-1] == 0:
                ni = nums.pop(i)
                res.append(ni)
            else:
                i += 1
        rest = self.largestDivisibleSubset(nums)
        return res if len(res) > len(rest) else rest

    def largestDivisibleSubset(self, nums):
        if len(nums) == 0: return []
        nums.sort()
        sol = [[num] for num in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(sol[i]) < len(sol[j]) + 1:
                    sol[i] = sol[j] + [nums[i]]
        return max(sol, key=len)
        
        