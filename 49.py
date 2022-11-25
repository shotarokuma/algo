class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = []
        ds = []
        for s in strs:
            d ={}
            for c in s:
                if c not in d:
                    d[c] = 1
                else:
                    d[c] += 1
            ds.append(d)
        while ds != []:
            j = 0
            target = ds.pop(0)
            curr = [strs.pop(0)]
            while j < len(ds):
                if ds[j] == target:
                    curr.append(strs.pop(j))
                    ds.pop(j)
                else:
                    j += 1
            res.append(curr)
        return res

    def sample(self, strs):
      hash = {}
      for s in strs:
         sortedS= ''.join(sorted(s))
         if sortedS in hash:
            hash[sortedS] += 1
         else:
            hash[sortedS] = 1
      return list(hash.values())



                    
                    
            
                
            
            
            
        