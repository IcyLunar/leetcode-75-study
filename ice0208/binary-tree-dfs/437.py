# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def go_down(self, cursor: TreeNode, num: list[int]):
        new_num = num + [num[-1] + cursor.val]

        for i in range(len(new_num) - 1):
            s = new_num[-1] - new_num[i]
            if s == self.targetSum:
                self.cnt += 1

        if cursor.left:
            self.go_down(cursor.left, new_num)
        if cursor.right:
            self.go_down(cursor.right, new_num)

    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.targetSum = targetSum
        self.cnt = 0

        if root:
            self.go_down(root, [0])

        return self.cnt
