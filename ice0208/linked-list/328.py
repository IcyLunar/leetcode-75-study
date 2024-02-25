# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head):
        if head == None or head.next == None:
            return head

        odd_head = head
        odd_tail = head
        even_head = head.next
        even_tail = head.next

        cursor = even_tail
        isOdd = True
        while cursor.next:
            cursor = cursor.next
            if isOdd:
                odd_tail.next = cursor
                odd_tail = cursor
            else:
                even_tail.next = cursor
                even_tail = cursor

            isOdd = not isOdd

        odd_tail.next = even_head
        even_tail.next = None

        return odd_head
