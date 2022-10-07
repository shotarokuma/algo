class Solution(object):
    def lengthOfLongestSubstring(self, s):
         """
        :type s: str
        :rtype: int
        """
         tmp = ""
         maxStr = ""
         for c in s:
            if tmp.find(c) != -1:
                maxStr = tmp if len(tmp) > len(maxStr) else maxStr
                tmp = tmp[tmp.find(c) + 1:] + c
            else:
                tmp += c
        
         return max(len(maxStr), len(tmp))

    def sample(self, s):
         ml = 0
         sub = []
         for i in range(len(s)):
            for j in range(i,len(s)):
              if s[j] in sub:
                  break
              sub.append(s[j])
            ml = max(ml, len(sub))
            sub = []
          
         return ml

        