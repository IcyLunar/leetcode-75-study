# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def go_down(self, cursor, leaf_list: list[int]):
        if not cursor.left and not cursor.right:
            leaf_list.append(cursor.val)
            return

        if cursor.left:
            self.go_down(cursor.left, leaf_list)
        if cursor.right:
            self.go_down(cursor.right, leaf_list)

    def leafSimilar(self, root1, root2) -> bool:
        leaf1, leaf2 = [], []

        if root1:
            self.go_down(root1, leaf1)
        if root2:
            self.go_down(root2, leaf2)

        return leaf1 == leaf2
