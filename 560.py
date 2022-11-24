class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        res = 0
        d = {0:1}
        curr = 0
        for n in nums:
            curr += n
            if curr - k in d:
                res += d[curr - k]
            if curr in d:
                d[curr] += 1
            else:
                d[curr] = 1
        return res
                
                
            
        
                
        