class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c == '(' or c == '{'or c == '[':
                stack.append(c)
            elif c == ')' :
                if len(stack) == 0 or stack.pop() != '(': return False
            elif c == '}':
                if len(stack) == 0 or stack.pop() != '{': return False
            elif c == ']':
                if len(stack) == 0 or stack.pop() != '[': return False
        
        if len(stack) == 0:
            return True
        else:
            return False
                
    def sample(self,s):
      d = {
        "(":")", "[":"]" ,"{":"}"
      }
      stack = []
      for x in s:
        if x in d:
          stack.append(x)
        elif stack:
          if x == d[stack[-1]]:
            stack.pop()
          else:
            return False
        else:
          return False
      return stack == []
          