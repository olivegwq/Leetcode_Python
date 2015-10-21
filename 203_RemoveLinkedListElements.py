# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        
        p1=head
        
        while p1.val==val:
            p1=p1.next
            if not p1:
                return p1
        head=p1
        p2=p1.next
        
        while p2:
            if p2.val==val:
                p1.next=p2.next
                p2=p1.next
            else:
                p1=p2
                p2=p2.next
        return head
