class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        def helper(grid, dp,h, v):
            if h >= m or v >= n or h < 0 or v < 0 or dp[v][h] or grid[v][h] == '0':
                return
            dp[v][h] = True
            helper(grid,dp, h + 1, v)
            helper(grid, dp, h, v + 1)
            helper(grid, dp, h - 1,v)
            helper(grid, dp, h, v - 1)
            
        n = len(grid)
        m = len(grid[0])
        res = 0
        dp = [[False for _ in range(m)]  for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if dp[i][j]:
                    continue
                if grid[i][j] == "0":
                    dp[i][j] = True
                else:
                    helper(grid, dp, j, i)
                    res += 1
        return res
                    