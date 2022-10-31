class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        words = set(wordDict)
        
        dp = [False] * (n + 1)
        dp[n] = True
        for i in range(n-1, -1, -1):
            for j in range(i + 1, n + 1):
                if dp[j] and s[i:j] in words:
                    dp[i] = True
                    break
        
        return dp[0]
                
            
        
            
        