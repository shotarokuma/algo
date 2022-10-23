class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        sort = sorted(nums)
        longSeq = 0
        seq = 1
        for i in range (0 ,len(nums) - 1):
            if sort[i + 1] == sort[i]:
                continue
            if sort[i + 1] - sort[i] == 1:
                seq += 1
                continue
            elif longSeq < seq:
                 longSeq = seq
            seq = 1
        
        return longSeq if seq < longSeq else seq

    def sample(self, nums):
        max_len = 0
        num_set = set(nums)
        for num in nums:
           if num - 1 not in num_set:
              curr_num = num
              curr_len = 1
           while curr_num + 1 in num_set:
              curr_num += 1
              curr_len += 1
           max_len = max(max_len,curr_len)
        return max_len


                