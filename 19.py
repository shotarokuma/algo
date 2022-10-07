# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        tmp = head
        stack = []
        
        while(tmp != None):
            stack.append(tmp)
            tmp = tmp.next
        
        stack.append(None)
        
        for i in range(1,n):
            stack.pop()
            
        last = stack.pop()
        stack.pop()
        if len(stack):
            new = stack.pop()
            new.next = last
        else:
            head = last
        
        return head

    def sample(self, head, n):
        def index(node):
          if not node:
            return 0
          i = index(node.next) + 1
          if i > n:
            node.next.val = node.val
            return i
          index(head)
          return head.next

        

