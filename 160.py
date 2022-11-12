class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        listMap = []
        while headA:
            listMap.append(headA)
            headA = headA.next
            
        listSet = set(listMap)
        while headB:
            if headB in listSet:
                return headB
            headB = headB.next
        return None
    
    def sample(self, headA, headB):
        one = headA
        two = headB

        while one != two:
            one = headB if not one else one.next
            two = headA if not two else two.next
        return one 
      

    
        