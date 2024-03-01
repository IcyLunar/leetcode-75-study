class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:

        edges = {(start, end) for start, end in connections}
        neighbors = {city: [] for city in range(n)}

        for s, e in connections:
            neighbors[s].append(e)
            neighbors[e].append(s)

        visit = [False] * n
        stack = [0]
        count = 0

        while stack:
            cur = stack.pop()
            visit[cur] = True
            for nxt in neighbors[cur]:
                if visit[nxt]:
                    continue
                visit[nxt] = True
                stack.append(nxt)

                if (cur, nxt) in edges:
                    count += 1

        return count


if __name__ == "__main__":
    testcase_list = [
        (6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]),
        (5, [[1, 0], [1, 2], [3, 2], [3, 4]]),
        (3, [[1, 0], [2, 0]]),
    ]

    for n, c in testcase_list:
        print(Solution().minReorder(n, c))
