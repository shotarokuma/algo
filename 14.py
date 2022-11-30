class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        i = 0
        res = ""
        while True:
            if i >= len(strs[0]):
                return res
            curr = strs[0][i]
            for st in strs:
                if i >= len(st) or st[i] != curr:
                    return res
            res += curr
            i += 1

    def sample(self, strs):
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest 
