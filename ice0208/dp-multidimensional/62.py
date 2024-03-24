class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] + [1 for _ in range(n)]

        for _ in range(m - 1):
            for i in range(1, n + 1):
                dp[i] += dp[i - 1]

        return dp[-1]


if __name__ == "__main__":
    print(Solution().uniquePaths(3, 7))
    print(Solution().uniquePaths(3, 2))
