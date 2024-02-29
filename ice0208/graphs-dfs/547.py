class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        provinces = 0

        visit = [False] * len(isConnected)
        for i in range(len(isConnected)):
            if visit[i]:
                continue
            provinces += 1
            stack = [i]

            while stack:
                cur = stack.pop()
                visit[cur] = True
                for idx, con in enumerate(isConnected[cur]):
                    if con == 1 and visit[idx] == False:
                        stack.append(idx)

        return provinces


if __name__ == "__main__":
    testcase_list = [
        [[1, 1, 0], [1, 1, 0], [0, 0, 1]],
        [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
    ]

    for testcase in testcase_list:
        print(Solution().findCircleNum(testcase))
