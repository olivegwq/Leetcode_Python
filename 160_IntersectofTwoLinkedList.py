# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        pt1,pt2=headA,headB
        
        while pt1 and pt2:
            pt1=pt1.next
            pt2=pt2.next
        
        if pt2 and not pt1:
            short=headA
            long=headB
            step=0
            while pt2:
                pt2=pt2.next
                step+=1
        else:
            short=headB
            long=headA
            step=0
            while pt1:
                pt1=pt1.next
                step+=1
        for i in range(step):
            long=long.next
        
        while long and short:
            if long==short:
                return long
            else:
                long=long.next
                short=short.next
        
        return long
        
