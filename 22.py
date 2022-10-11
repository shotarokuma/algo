


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        res = []
        
        def helper(n, curr, res):
            if len(curr) == (n * 2):
                res.append(curr)
            if curr.count("(") < n:
                helper(n, curr + "(", res)
            if curr.count("(") > curr.count(")"):
                helper(n, curr + ")", res)
        
        helper(n, "", res)
        return res
      
    def sample(self, n):
        result = []
        self.backTrack(n, result,[], 0,0)
        return result

    def backTrack(self, n, result,subset, left, right ):
        if(len(subset) == 2 * n):
          result.append("".join(subset))
        
        if left < n:
          subset.append("(")
          self.backTrack(n, result, subset, left + 1, right)
          subset.pop()
        if right < left:
          subset.append(")")
          self.backTrack(n, result, subset, left, right + 1)
          subset.pop()
