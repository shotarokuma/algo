class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        def helper(candidates, target, curr, res):
            if sum(curr) == target:
                sorted(curr)
                res.append(curr)
                return
            if sum(curr) > target:
                return
            
            for c in candidates:
                if curr == [] or c >= curr[-1]:
                    helper(candidates, target, curr + [c], res)

        def dfs(nums, target, path, ret):
          if target < 0:
            return 
          if target == 0:
            ret.append(path)
            return
          for i in range(len(nums)):
            dfs(nums[i:], target - nums[i], path+[nums[i]], ret)
            
                
        
        res = []
        curr = []
        helper(candidates, target, curr, res)
        return  res