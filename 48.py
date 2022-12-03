import math


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        start = 0
        while start < n /2:
            tmp= []
            rem = matrix[n - 1 - start][start]
            for i in range(start + 1, n - start):
                tmp.append(matrix[start][i])
            for i in range(start + 1,  n - start):
                tmp.append(matrix[i][n - 1 - start])
                matrix[i][n - 1 - start] = tmp.pop(0)
            for i in reversed(range(start, n - start - 1)):
                tmp.append(matrix[n - 1 - start][i])
                matrix[n - 1 - start][i] = tmp.pop(0)
            for i in reversed(range(start, n - start - 1)):
                tmp.append(matrix[i][start])
                matrix[i][start] = tmp.pop(0)
            for i in range(start + 1, n - start):
                matrix[start][i] = tmp.pop(0)
            matrix[start][start] = rem
            start += 1

        def sample(self, matrix):
          n = len(matrix)
          for row in range(math.ceil(n / 2)):
            for col in range(int(n - n/ 2)):
              (
				        matrix[row][col],
				        matrix[~col][row],
				        matrix[~row][~col],
				        matrix[col][~row],
			        ) = (
				        matrix[~col][row],
				        matrix[~row][~col],
				        matrix[col][~row],
				        matrix[row][col],
                )
              
                
                
            
        