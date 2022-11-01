class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cmin = float('inf')
        cmax = float('-inf')
        curr = float('-inf')
        for n in nums:
            if n < 0:
                cmin, cmax = cmax, cmin
            cmin *= n
            cmin = min(n, cmin)
            cmax *= n
            cmax = max(n, cmax)
            curr = max(curr, cmax)
        return curr
            
        