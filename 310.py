class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        def helper(i, visit):
            if visit[i]:
                return -1
            visit[i] = True
            res = 0
            for e in edges:
                if i in e:
                    v = e[0] if e.index(i) == 1 else e[1]
                    res = max(res, helper(v, visit) + 1)
            return res

        if n == 2:
            return [0, 1]
            
        degree = []
        for i in range(0, n):
            degree.append([i, 0])
        for e in edges:
            degree[e[0]][1] += 1
            degree[e[1]][1] += 1
        sDegree = sorted(degree, reverse=True, key=lambda x: x[1]) 
        res = []
        mh = float("inf")
        for sd in sDegree:
            if sd[1] == 1:
                break
            visit = [False] * n
            h = helper(sd[0] , visit)
            if mh  > h:
                mh = h
                res = [sd[0]]
            elif mh == h:
                res.append(sd[0])
        return res

    def sample(self, n, edges):
      if n == 1: return [0]
        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        queue, degrees = [], {}
        for node, neighbors in adj.items():
            degrees[node] = len(neighbors)
            # Insert all leaves into our priority queue.
            if degrees[node] == 1:
                queue.append(node)
        ans = []
        while queue:
            nodes = []
            while queue:
                nodes.append(queue.pop())
            ans = nodes
            for node in nodes:
                degrees[node] -= 1
                for neighbor in adj[node]:
                    degrees[neighbor] -= 1
                    if degrees[neighbor] == 1:
                        queue.append(neighbor)
        return ans

            
