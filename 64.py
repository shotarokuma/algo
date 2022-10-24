class Solution(object):
    def minPathSum(self, grid):
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        tmp = 0
        for i in range(len(grid)):
            dp[i][0] = tmp + grid[i][0]
            tmp = dp[i][0]
        tmp = 0
        for i in range(len(grid[0])):
            dp[0][i] = tmp + grid[0][i]
            tmp = dp[0][i]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                prev = min(dp[i - 1][j], dp[i][j - 1])
                dp[i][j] = prev + grid[i][j]
    
        return dp[-1][-1]

    def sample(self, grid):
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                dp[row][col] = grid[row][col]
                if row == 0 and col == 0:
                    continue
                candidates = set()
                if col > 0:
                    candidates.add(dp[row][col - 1])
                if row > 0:
                    candidates.add(dp[row - 1][col])
                print(candidates)
                dp[row][col]+=min(candidates)
        return dp[-1][-1]