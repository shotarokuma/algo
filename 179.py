class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def helper(n1, n2):
            s1 = str(n1) + str(n2)
            s2 = str(n2) + str(n1)
            if s1 > s2:
                return -1
            else:
                return 1
        res = ""
        d = {}
        for n in nums:
            tmp = str(n)
            if not tmp[0] in d:
                d[tmp[0]] = [n]
            else:
                d[tmp[0]].append(n)
        for i in reversed(range(0, 10)):
            strI = str(i)
            if strI in d:
                d[strI] = sorted(d[strI], key=cmp_to_key(helper))
                while d[strI] != []:
                    tmp = d[strI].pop(0)
                    res += str(tmp)
        return res if res[0] != "0" else "0"