# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = []
        tmp = head
        while tmp:
            if tmp in curr:
                return tmp
            curr.append(tmp)
            tmp = tmp.next
        return None

    def sample(self, head):
        if head is None:
          return None
        slow, fast, start = head, head, head
        while fast.next and fast.next.next:
              slow = slow.next
              fast =  fast.next.next
              if slow == fast:
                while start != slow:
                  slow = slow.next
                  start = start.next
                return start
        return None
