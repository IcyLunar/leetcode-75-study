from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        answer = []
        q = deque()

        if root:
            q.append((root, 1))

        while q:
            cursor, i = q.popleft()
            if i > len(answer):
                answer.append(cursor.val)
            else:
                answer[i - 1] = cursor.val

            if cursor.left:
                q.append((cursor.left, i + 1))
            if cursor.right:
                q.append((cursor.right, i + 1))

        return answer
