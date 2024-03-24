# 배열을 이용하여 O(n^2)으로 풀었으나, 시간 초과로 실패
# https://youtu.be/OVsAAgy6awk?si=8mUIyc-XDneMYkew


class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        notHold = 0  # 주식을 가지고 있지 않을 때의 최대 이익
        hold = float("-inf")  # 주식을 가지고 있을 때의 최대 이익

        for price in prices:
            newHold = max(hold, notHold - price - fee)
            newNotHold = max(notHold, hold + price)

            notHold, hold = newNotHold, newHold

        return notHold


if __name__ == "__main__":
    print(Solution().maxProfit([1, 3, 2, 8, 4, 9], 2))
    print(Solution().maxProfit([1, 3, 7, 5, 10, 3], 3))
