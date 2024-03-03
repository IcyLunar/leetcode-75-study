# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def down(self, cursor, depth):
        self.max_depth = max(self.max_depth, depth)

        if cursor.left:
            self.down(cursor.left, depth + 1)
        if cursor.right:
            self.down(cursor.right, depth + 1)

    def maxDepth(self, root) -> int:
        self.max_depth = 0

        if root:
            self.down(root, 1)

        return self.max_depth
