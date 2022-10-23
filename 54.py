class Solution(object):
    def helper(self, trace):
        for i in trace:
            for j in i:
                if not j:
                    return True
        return False
                    
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == None:
            return []
            
        res = []
        m = 0
        n = 0
        M = len(matrix[0])
        N = len(matrix)
        trace = [[False]*M for i in range(N)]
        res.append(matrix[0][0])
        trace[0][0] = True
        while self.helper(trace):
            while m < M - 1 and not trace[n][m + 1]:
                m += 1
                res.append(matrix[n][m])
                trace[n][m] = True
                
            while n < N - 1 and not trace[n + 1][m]:
                n += 1
                res.append(matrix[n][m])
                trace[n][m] = True
            
            while m >= 1 and not trace[n][m - 1]:
                m -= 1
                res.append(matrix[n][m])
                trace[n][m] = True
            
            while not trace[n - 1][m]:
                n -= 1
                res.append(matrix[n][m])
                trace[n][m] = True
        
        return res

    def sample(self, matrix):
      out = []
      while matrix:
        out += matrix.pop(0)
        if matrix:
          for i in range(len(matrix) - 1):
            if len(matrix[i]) != 0:
              out.append(matrix[i].pop())
        if matrix:
          out += matrix.pop()[::-1]
        if matrix:
          for i in range(1, len(matrix) + 1):
            if len(matrix[-i]) != 0:
              out.append(matrix[-i].pop(0))
        
        return out

          
                
                
        