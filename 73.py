class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        dp = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0 and not dp[i][j]:
                    for k in range(n):
                        if matrix[i][k] != 0:
                            matrix[i][k] = 0
                            dp[i][k] = True
                    for k in range(m):
                        if matrix[k][j] != 0:
                            matrix[k][j] = 0
                            dp[k][j] = True

    def sample(self, matrix):
      if not matrix:
        return []
      
      m = len(matrix)
      n = len(matrix[0])

      zero_row = [False] * m
      zero_col = [False] * n
      for row in range(m):
        for col in range(n):
          if matrix[row][col] == 0:
            zero_col[col] = 0
            zero_row[row] = 0
      
      for row in range(m):
        for col in range(n):
          if zero_row[row] or zero_col[col]:
            matrix[row][col] = 0