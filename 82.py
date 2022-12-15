# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        while head and head.next and head.val == head.next.val:
            while head and head.next and head.val == head.next.val:
                head = head.next
            head = head.next
        tmp = head
        while tmp and tmp.next:
            curr = tmp.next
            if curr.next and curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                tmp.next = curr.next
            else:
                tmp = tmp.next
        return head
        
    def sample(self, head):
        sentinel = ListNode(0, head)
        pred = sentinel
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                pred.next = head.next 
            else:
                pred = pred.next 
            head = head.next
            
        return sentinel.next
