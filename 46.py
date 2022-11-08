class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def deepCopy(nums):
            clone = []
            for n in nums:
                clone.append(n)
            return clone
        res = []
        stack = []
        for n in nums:
            stack.append([n])
            
        m = len(nums)
        while stack != []:
            tmp = stack.pop()
            if len(tmp) == m:
                res.append(tmp)
            for n in nums:
                if n not in tmp:
                    clone = deepCopy(tmp)
                    clone.append(n)
                    stack.append(clone)
        return res

    def sample(self, nums):
        return [ [elem] + permu  for idx, elem in enumerate(nums) for permu in self.sample(nums[:idx] + nums[idx+1:] ) ] or [ [] ]
                    
            
        
        
        
            