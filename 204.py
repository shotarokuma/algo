class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n < 2:
            return 0
        dp = [True for _ in range(0, n)]
        dp[0] = False
        dp[1] = False
        prev = 2
        for i in range(2, n):
            if not dp[i]:
                continue
            curr = i * prev
            prev = i
            while curr < n:
                dp[curr] = False
                curr += i
        return sum(dp)