# Definition for singly-linked list.
from typing import List


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head 
        tmp = head 
        length = 0
        while tmp:
            length += 1
            tmp = tmp.next
        tmp = head
        for i in range(0, length / 2 - 1):
            tmp = tmp.next
        right = self.sortList(tmp.next)
        tmp.next = None
        left = self.sortList(head)
        if left.val < right.val:
            newHead =  ListNode(left.val)
            left = left.next
        else:
            newHead = ListNode(right.val)
            right = right.next
        tmp = newHead
        while left or right:
            if not left:
                tmp.next = right
                break
            elif not right:
                tmp.next = left
                break
            if  left.val < right.val:
                tmp.next =  ListNode(left.val)
                left = left.next
            else:
                tmp.next = ListNode(right.val)
                right = right.next
            tmp = tmp.next
        return newHead

            
    def sample(self, head):
        if head is None:
           return
        arr = []
        while head:
              arr.append(head.val)
              head = head.next
        arr.sort()
        dummy = curr = ListNode(0)
        for i in arr:
            temp = ListNode(i)
            curr.next = temp
            curr = curr.next
        return dummy.next