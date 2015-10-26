# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        dummy=ListNode(0)
        dummy.next=head
        pos,current=dummy,head
        while current and current.next:
            pre=current.next.next
            pos.next,current.next.next,current.next=current.next,current,pre
            pos=pos.next.next
            current=pos.next
        return dummy.next
