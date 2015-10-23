# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        
        slow=ListNode(0)
        slow.next=head
        fast=head
        pre=slow.next
        pos=None
        
        while fast and fast.next:
            slow.next=pos
            pos=slow
            slow=pre
            pre=pre.next
            fast=fast.next.next
        
        if not fast:
            fast=pre
        else:
            fast=pre.next
        
        while fast:
            if fast.val!=slow.val:
                return False
            fast=fast.next
            pre=slow
            slow=pos
            pos=pos.next
            slow.next=pre
        return True
        
