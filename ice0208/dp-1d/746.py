MAX_COST = 1_000_000


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        cost = cost + [0, 0]
        dp = [MAX_COST for _ in range(len(cost))]
        dp[0], dp[1] = cost[0], cost[1]

        for i in range(len(cost) - 2):
            dp[i + 1] = min(dp[i + 1], dp[i] + cost[i + 1])
            dp[i + 2] = min(dp[i + 2], dp[i] + cost[i + 2])

        return min(dp[-2:])


if __name__ == "__main__":
    print(Solution().minCostClimbingStairs([10, 15, 20]))
    print(Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
