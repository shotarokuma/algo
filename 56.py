class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        intervals = sorted(intervals, key=lambda x:(x[0]))
        
        i = 0
        while i < len(intervals) - 1:
            curr = intervals[i]
            nextInt = intervals[i + 1]
            if curr[0] <= nextInt[1] and nextInt[0] <= curr[1]:
                merged = [curr[0], max(curr[1], nextInt[1])]
                intervals.pop(i)
                intervals[i] = merged
            else:
                i +=  1
                
        return intervals
            