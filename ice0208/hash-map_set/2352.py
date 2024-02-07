class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        s = dict()

        for r in range(len(grid)):
            t = ""
            for c in range(len(grid)):
                t += str(grid[r][c]) + ","
            s[t] = s.get(t, 0) + 1

        answer = 0
        for c in range(len(grid)):
            t = ""
            for r in range(len(grid)):
                t += str(grid[r][c]) + ","
            if t in s:
                answer += s[t]

        return answer


if __name__ == "__main__":
    testcase_list = [
        [[3, 2, 1], [1, 7, 6], [2, 7, 7]],
        [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]],
    ]

    for testcase in testcase_list:
        print(Solution().equalPairs(grid=testcase))
