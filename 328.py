# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        odd = head
        even = head.next
        tmp = even
        while odd.next and even.next:
            if odd.next.next:
                odd.next = odd.next.next
                odd = odd.next
            if even.next.next:
                even.next = even.next.next
                even = even.next
        even.next = None
        odd.next = tmp
        return head

    def sample(self, head):
        if not head or not head.next:
            return head
        odd = head
        even = head.next
        tmp = even
        while odd and even and even.next:
            odd.next = even.next
            odd = odd.next
            if odd:
                even.next = odd.next
                even = even.next
        odd.next = tmp
        return head

            
            
        