class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        prev = 1
        res = 2
        for i in range(2, n):
            tmp = res
            res = res + prev
            prev = tmp
        return res