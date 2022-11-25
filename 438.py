class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        d = {}
        for c in p:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        i = 0
        m = len(s)
        n = len(p)
        res = []
        while i < m:
            while i < m and s[i] not in d: i += 1
            if i >= m: break
            tmp = {}
            j = i
            while j < m and s[j] in d:
                if s[j] not in tmp:
                    tmp[s[j]] = 1
                else:
                    tmp[s[j]] += 1
                if tmp[s[j]] > d[s[j]]:
                    while s[i] != s[j]:
                        tmp[s[i]] -= 1
                        i += 1
                    tmp[s[i]] -= 1
                    i += 1
                j += 1
                if j - i >= n:
                    res.append(i)
                    tmp[s[i]] -= 1
                    i += 1
            i = j
        return res
    def sample(self, s, p):
      n1, n2 = len(s), len(p)
      d1 = Counter(p)
      d2 = Counter(s[:n2 -1])
      ans = []
      j = 0
      for i in range(n2-1, n1):
        d2[s[i]] += 1
        if d1 == d2:
          ans.append(j)
        d2[s[j]] -= 1
        if d2[s[j]] == 0:
          del d2[s[j]]
        j += 1
      return ans
            
            
            