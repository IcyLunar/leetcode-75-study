# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def go_down(self, cursor: TreeNode):
        p_f, q_f = False, False
        if cursor.val == self.p.val:
            p_f = True
        if cursor.val == self.q.val:
            q_f = True

        if cursor.left:
            p_f2, q_f2 = self.go_down(cursor.left)
            p_f = p_f or p_f2
            q_f = q_f or q_f2
            if p_f == q_f == True and self.answer == None:
                self.answer = cursor
        if cursor.right:
            p_f2, q_f2 = self.go_down(cursor.right)
            p_f = p_f or p_f2
            q_f = q_f or q_f2
            if p_f == q_f == True and self.answer == None:
                self.answer = cursor

        return (p_f, q_f)

    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        self.p, self.q = p, q
        self.answer = None

        if root:
            self.go_down(root)

        return self.answer if self.answer else root
