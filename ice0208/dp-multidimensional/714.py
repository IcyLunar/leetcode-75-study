class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        buy = float("-inf")
        sell = 0

        for price in prices:
            buy, sell = max(buy, sell - price), max(sell, buy + price - fee)

        return sell


if __name__ == "__main__":
    print(Solution().maxProfit([1, 3, 2, 8, 4, 9], 2))
    print(Solution().maxProfit([1, 3, 7, 5, 10, 3], 3))
