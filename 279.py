class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(n, dp):
            i = int(n ** 0.5)
            res = float('inf')
            while i > 0:
                res = min(dp[n - (i * i)] + 1, res)
                i -= 1
            return res

        dp = [0, 1]
        for i in range(2, n + 1):
            dp.append(helper(i, dp))
        return dp[n]
    
    def sample(self, n):
        dp = [0]
        perfectSq = [pow(i,2) for i in range(1, int(sqrt(n))+1)]
        while len(dp) < n+1:
            dpI = inf
            for ps in perfectSq:
                if len(dp)<ps: break
                dpI = min(dpI,1+dp[-ps])
            dp.append(dpI)
        return dp[n]

                