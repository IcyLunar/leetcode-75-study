# Trie 구현을 다시 연습해보면서 이 문제에 적용시켜보았다.
# 시간 복잡도가 굉장히 높게 나오는데 더 좋은 방법이 있는지 찾아봐야겠다.


class TreeNode:
    val, next_tree_nodes, end_of_string = [None] * 3

    def __init__(self, val: str):
        self.val = val
        self.next_tree_nodes = [None for _ in range(ord("z") - ord("a") + 1)]
        self.end_of_string = False


class Tree:
    def __init__(self):
        self.root = TreeNode(-1)

    def add(self, string: str):
        cur = self.root
        for char in string:
            char_index = ord(char) - ord("a")
            if cur.next_tree_nodes[char_index] is None:
                cur.next_tree_nodes[char_index] = TreeNode(char)
            cur = cur.next_tree_nodes[char_index]
        cur.end_of_string = True

    def search(self, string):
        cur = self.root
        for c in string:
            c_index = ord(c) - ord("a")
            if cur.next_tree_nodes[c_index] == None:
                return []
            cur = cur.next_tree_nodes[c_index]

        results = []
        if cur.end_of_string == True:
            results.append(string)
        self.search_dfs(cur, string, results)
        return results

    def search_dfs(self, cur_node: TreeNode, string: str, results_list: list):

        for next_tree_node in cur_node.next_tree_nodes:
            if next_tree_node == None:
                continue

            if next_tree_node.end_of_string:
                results_list.append(string + next_tree_node.val)
            self.search_dfs(next_tree_node, string + next_tree_node.val, results_list)


class Solution:
    def suggestedProducts(
        self, products: list[str], searchWord: str
    ) -> list[list[str]]:
        myTree = Tree()

        for product in products:
            myTree.add(product)

        results = []
        cur_string = ""
        for searchChar in searchWord:
            cur_string += searchChar
            results.append(myTree.search(cur_string)[:3])

        return results


if __name__ == "__main__":
    print(
        Solution().suggestedProducts(
            products=["mobile", "mouse", "moneypot", "monitor", "mousepad"],
            searchWord="mouse",
        )
    )
    print(Solution().suggestedProducts(products=["havana"], searchWord="havana"))
