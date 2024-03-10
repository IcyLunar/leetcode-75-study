# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        cursor = root
        while cursor != None:
            if cursor.val == val:
                return cursor

            if val < cursor.val:
                cursor = cursor.left
            else:
                cursor = cursor.right

        return None
