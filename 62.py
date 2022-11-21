class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(n):
            dp[0][i] = 1
        for i in range(m):
            dp[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[-1][-1]
            
    def sample(self, m, n):
        def helper(i, j):
          if i >= m or j >= n:return 0
          if i == m - 1 and j == n - 1:return 1
          return helper(i + 1, j) + helper(i, j + 1)
        return helper(0,0)