# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def go_down(self, cursor: TreeNode, max_value: int):
        if cursor.val >= max_value:
            self.cnt += 1
        max_value = max(max_value, cursor.val)

        if cursor.left:
            self.go_down(cursor.left, max_value)
        if cursor.right:
            self.go_down(cursor.right, max_value)

    def goodNodes(self, root: TreeNode) -> int:
        self.cnt = 0

        if root:
            self.go_down(root, -(10**4))

        return self.cnt
