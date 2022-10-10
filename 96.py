class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        sol = [1] * (n + 1)
        for i in range(2 , n+ 1):
            total = 0
            for j in range(0,i):
                total += sol[j] * sol[i - j - 1]
            sol[i] = total
        
        return sol[n]
                