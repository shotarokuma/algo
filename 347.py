from typing import Counter


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        data = {}
        while nums != []:
            i, freq = 1, 1
            while i  < len(nums):
                if nums[0] == nums[i]:
                    freq += 1
                    nums.pop(i)
                else:
                    i += 1
            data.update({nums[0]: freq})
            nums.pop(0)
        res = []
        for i in range(k):
            target = max(data, key=data.get)
            res.append(target)
            data.pop(target)  
        return res
    
    def sample(self,nums,k):
        cnt = Counter(nums)
        n = len(nums)
        bucket = [[] for _ in range(n + 1)]
        for nums, freq in cnt.items():
            bucket[freq].append(nums)
        
        bucketIdx = n
        ans = []
        while k > 0:
            while not bucket[bucketIdx]:
                bucketIdx -= 1
            
            for num in bucket[bucketIdx]:
                if k == 0:break
                ans.append(num)
                k -= 1
            bucketIdx -= 1
        return ans

                    
                