class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        res = ""
        i = 0
        while i < len(s):
            if ord(s[i]) >= 49 and ord(s[i]) <= 57:
                num = ""
                while s[i] != "[":
                    num += s[i]
                    i += 1
                i += 1
                start = i
                nest = 0
                while s[i] != "]" or  nest != 0:
                    if s[i] == "[":
                        nest += 1
                    if s[i] == "]":
                        nest -= 1
                    i += 1
                part = self.decodeString(s[start:i])
                for j in range(0, int(num)):
                    res += part 
            else:
                res += s[i]
            i += 1
        return res

    def sample(self, s):
        curr_s = ""
        curr_n = 0
        stack = []
        for char in s:
          if char.isdisit():
             curr_n = curr_n * 10 + int(char)
          elif char == "[":
             stack.append((curr_s, curr_n))
             curr_s = ""
             curr_n = 0
          elif char == "]":
             prev_s , prev_n = stack.pop()
             curr_s = prev_s + prev_n * curr_s
          else:
            curr_s += char
        return curr_s