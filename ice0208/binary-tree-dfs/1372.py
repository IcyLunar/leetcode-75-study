# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def go_down(self, cursor: TreeNode, wasRight: int, cnt: int):
        self.answer = max(self.answer, cnt)

        if wasRight == -1:
            left_cnt, right_cnt = 1, 1
        elif wasRight == 0:
            left_cnt, right_cnt = 1, cnt + 1
        else:
            left_cnt, right_cnt = cnt + 1, 1

        if cursor.left:
            self.go_down(cursor.left, 0, left_cnt)
        if cursor.right:
            self.go_down(cursor.right, 1, right_cnt)

    def longestZigZag(self, root: TreeNode) -> int:
        self.answer = 0

        if root:
            self.go_down(root, 0, 0)

        return self.answer
