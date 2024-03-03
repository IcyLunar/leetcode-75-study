# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        if head == None or head.next == None:
            return head

        prev = head
        cur = head.next
        head.next = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        return prev
