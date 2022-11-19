"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return
        q = [[root]]
        while q:
            curr = q.pop(0)
            tmp = []
            for c in curr:
                tmp.append(c.left)
                tmp.append(c.right)
            if not None in tmp:
                for i in range(len(tmp) - 1):
                    tmp[i].next = tmp[i + 1]
                tmp[-1].next = None
                q.append(tmp)
        return root