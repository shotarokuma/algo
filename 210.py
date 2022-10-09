class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        edges = [0] * numCourses
        for pre in prerequisites:
            edges[pre[0]] += 1
        
        res = []
        queue = []
        
        for i in range(0, numCourses):
            if edges[i] == 0:
                queue.append(i)
        
        while len(queue) != 0:
            target = queue.pop(0)
            res.append(target)
            for pre in prerequisites:
                if target == pre[1]:
                    edges[pre[0]] -= 1
                    if edges[pre[0]] == 0:
                        queue.append(pre[0])
        
        if len(res) != numCourses:
            return []
        else:
            return res
            
                
                
                
           
        