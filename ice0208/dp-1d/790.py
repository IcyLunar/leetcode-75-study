MOD = 10**9 + 7


class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5

        dp = [0 for _ in range(n)]
        dp[0], dp[1], dp[2] = 1, 2, 5

        s = 1
        for i in range(3, n):
            dp[i] = (dp[i - 2] + dp[i - 1] + dp[i - 3] * 2 + s * 2) % MOD
            s += dp[i - 3]

        return dp[-1]
