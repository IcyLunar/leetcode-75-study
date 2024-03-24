class Solution:
    def __init__(self):
        self.mapping = dict()

        cur = ord("a")
        for i in range(2, 10):
            key = str(i)
            self.mapping[key] = []

            iterate_cnt = 3
            if i in (7, 9):
                iterate_cnt = 4
            for _ in range(iterate_cnt):
                self.mapping[key].append(chr(cur))
                cur += 1

    def __backtracking(self, i: int, digits: str, cur: str):
        if i == len(digits):
            self.answer.append(cur)
            return

        for value in self.mapping[digits[i]]:
            self.__backtracking(i + 1, digits, cur + value)

    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        self.answer = []

        self.__backtracking(0, digits, "")

        return self.answer


if __name__ == "__main__":
    print(Solution().letterCombinations("23"))
    print(Solution().letterCombinations(""))
    print(Solution().letterCombinations("2"))
