class Solution:
    def __backtracking(self, i: int, curSum: int, lst: list[int]):
        if i > self.k:
            if curSum == self.n:
                self.answer.append(lst)
            return

        for nxt in range(lst[-1] + 1 if lst else 1, 10):
            self.__backtracking(i + 1, curSum + nxt, [*lst, nxt])

    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        self.k, self.n = k, n
        self.answer = []
        self.__backtracking(1, 0, [])
        return self.answer


if __name__ == "__main__":
    print(Solution().combinationSum3(k=3, n=7))
    print(Solution().combinationSum3(k=3, n=9))
    print(Solution().combinationSum3(k=4, n=1))
