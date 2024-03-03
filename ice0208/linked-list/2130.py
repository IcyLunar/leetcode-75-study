# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head):
        length = 1

        cur = head
        while cur.next:
            length += 1
            cur = cur.next

        twin_sum = []

        cur = head
        i = 0
        while cur:
            if i < length // 2:
                twin_sum.append(cur.val)
            else:
                twin_sum[length - i - 1] += cur.val

            cur = cur.next
            i += 1

        answer = max(twin_sum)

        return answer
