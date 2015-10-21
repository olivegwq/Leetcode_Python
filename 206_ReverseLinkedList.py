# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        if not head.next:
            return head
        
        pos,cur, pre=head,head.next,head.next.next
        
        while pre:
            cur.next=pos
            pos,cur,pre=cur,pre,pre.next
        cur.next=pos
        head.next=None
        head=cur
        return head
        
