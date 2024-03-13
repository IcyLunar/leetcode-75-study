class Solution:
    def __init__(self):
        self.cach = dict()

    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        if n not in self.cach:
            self.cach[n] = (
                self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
            )

        return self.cach[n]


if __name__ == "__main__":
    print(Solution().tribonacci(4))
