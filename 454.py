class Solution(object):
   def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        def helper(nums):
            d = {}
            for n in nums:
                if not n in d:
                    d[n] = 1
                else:
                    d[n] += 1
            return d
        
        d1 = helper(nums1)
        d2 = helper(nums2)
        d3 = helper(nums3)
        d4 = helper(nums4)
        nums1 = sorted(list(set(nums1)))
        nums2 = sorted(list(set(nums2)))
        nums3 = sorted(list(set(nums3)))
        nums4 = sorted(list(set(nums4)))
        d12 = {}
        res = 0
        for n1 in nums1:
            for n2 in nums2:
                if n1 + n2 in d12:
                    d12[n1 + n2] += d1[n1] * d2[n2]
                else:
                    d12[n1 + n2] =  d1[n1] * d2[n2]
        for n3 in nums3:
            for n4 in nums4:
                curr = (n3 + n4) * (-1)
                if curr in d12:
                    res += d12[curr] * d3[n3] * d4[n4]
        return res
    
    def sample(self, nums1, nums2, nums3, nums4):
      n,dict1,ans = len(nums1),{},0
      for a in range(n):
            for b in range(n):
                if nums1[a]+nums2[b] not in dict1:
                    dict1[nums1[a]+nums2[b]]=1
                else:
                    dict1[nums1[a]+nums2[b]]+=1
      for a in range(n):
            for b in range(n):
                if 0-(nums3[a]+nums4[b]) in dict1:
                    ans+= dict1[0-(nums3[a]+nums4[b])]      
      return ans
