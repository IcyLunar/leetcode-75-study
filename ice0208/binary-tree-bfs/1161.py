from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        q = deque()
        sum_of_x_level = dict()

        max_sum = root.val
        answer = 1

        q.append((root, 1))

        while q:
            cursor, level = q.popleft()
            sum_of_x_level[level] = sum_of_x_level.get(level, 0) + cursor.val

            if cursor.left:
                q.append((cursor.left, level + 1))
            if cursor.right:
                q.append((cursor.right, level + 1))

        for k, v in sum_of_x_level.items():
            if v > max_sum:
                answer = k
                max_sum = v
        return answer
