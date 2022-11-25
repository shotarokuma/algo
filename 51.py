class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        
        def helper(tmp,i,j):
            if len(tmp) == 0:
                return True
            for k in range(i):
                if tmp[k][j] == 'Q':
                    return False
            tmpi = i - 1
            tmpj = j - 1
            while tmpi >= 0 and tmpj >= 0:
                if tmp[tmpi][tmpj] == "Q":
                    return False
                tmpi -= 1
                tmpj -= 1
            tmpi = i- 1
            tmpj = j + 1
            while tmpi >= 0 and tmpj < len(tmp[0]):
                if tmp[tmpi][tmpj] == "Q":
                    return False
                tmpi -= 1
                tmpj += 1
            return True     
            
        
        res = []
        tmp = []
        i = 0
        j = 0
        while i < n:
            while j < n:
                if i >= n and j >= n:
                    res.append(list(tmp))
                    prev = tmp.pop()
                    j = prev.index('Q') + 1
                    i -= 1
                    while j >= n and len(tmp) != 0:
                        prev = tmp.pop()
                        j = prev.index('Q') + 1
                        i -= 1  
                    continue
                if helper(tmp, i, j):
                    row = ""
                    for k in range(n):
                        if k == j:
                            row += "Q"
                        else:
                            row += "."
                    tmp.append(row)
                    j = 0
                    i += 1
                else:
                    j += 1
                if j > n:
                    prev = tmp.pop()
                    j = prev.index('Q') + 1
                    i -= 1
                    while j >= n and len(tmp) != 0:
                        prev = tmp.pop()
                        j = prev.index('Q') + 1
                        i -= 1      
        return res
                    
                    
                    
                    
            
                    
                
        