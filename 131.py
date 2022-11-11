class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def checker(s):
            left = 0
            right = len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        def helper(s, res, curr):
            if not s:
                res.append(list(curr))
                return 
            
            for i in range(1,len(s) + 1):
                if checker(s[:i]):
                    curr.append(s[:i])
                    helper(s[i:], res, curr)
                    curr.pop()
                    
        res = []
        helper(s, res, [])
        return res