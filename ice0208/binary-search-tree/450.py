from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        parent_of_root = TreeNode(-1, root, None)

        # 삭제할 노드와 삭제할 노드의 부모를 찾습니다.
        parent_of_cursor = parent_of_root
        cursor = root

        parent_of_will_remove_node = None
        will_remove_node = None
        while cursor:
            if key < cursor.val:
                parent_of_cursor = cursor
                cursor = cursor.left
            elif key > cursor.val:
                parent_of_cursor = cursor
                cursor = cursor.right
            else:
                parent_of_will_remove_node = parent_of_cursor
                will_remove_node = cursor
                break

        # 삭제할 노드를 못찾았을 때
        if will_remove_node == None:
            return root

        # 지울 노드의 왼쪽에 노드가 있을 때
        if will_remove_node.left:
            parent_of_cursor = will_remove_node
            cursor = will_remove_node.left

            # 왼쪽 -> 오른쪽 패턴
            if not cursor.right:
                will_remove_node.val = cursor.val
                will_remove_node.left = cursor.left
            else:
                while cursor.right:
                    parent_of_cursor = cursor
                    cursor = cursor.right

                will_remove_node.val = cursor.val
                parent_of_cursor.right = cursor.left

        elif will_remove_node.right:
            parent_of_cursor = will_remove_node
            cursor = will_remove_node.right

            # 오른쪽 -> 왼쪽 패턴
            if not cursor.left:
                will_remove_node.val = cursor.val
                will_remove_node.right = cursor.right
            else:
                while cursor.left:
                    parent_of_cursor = cursor
                    cursor = cursor.left

                will_remove_node.val = cursor.val
                parent_of_cursor.left = cursor.right

        # 양쪽 노드가 없음
        else:
            if (
                parent_of_will_remove_node.left
                and parent_of_will_remove_node.left.val == will_remove_node.val
            ):
                parent_of_will_remove_node.left = None
            else:
                parent_of_will_remove_node.right = None

        return parent_of_root.left
