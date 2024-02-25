# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head):
        # Linked List의 길이 구하기
        len = 1
        cursor = head
        while cursor.next:
            len += 1
            cursor = cursor.next

        # 길이가 1일 때, None을 return
        if len == 1:
            return None

        # middle의 index 구하기
        middle_index = len // 2

        # cursor prev -> cursor next 로 연결해서 middle 값을 제거
        cursor_index = 0
        cursor = head
        cursor_prev = None
        while cursor_index < middle_index:
            cursor_index += 1
            cursor_prev = cursor
            cursor = cursor.next

        middle_prev_cursor = cursor_prev
        middle_cursor = cursor

        # middle 노드 연결 끊기
        middle_prev_cursor.next = middle_cursor.next
        middle_cursor.next = None

        return head
