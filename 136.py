class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = []
        for n in nums:
            if n not in tmp:
                tmp.append(n)
            else:
                tmp.remove(n)
        return tmp[0]
    
    def sample(self, nums):
        occur = set()
        for n in nums:
            if n in occur: occur.remove(n)
            else: occur.add(n)
        return list(occur)[0]
                
            
        