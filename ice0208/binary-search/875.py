import math


class Solution:
    def getNeedHour(self, piles: list[int], k: int):
        answer = 0
        for pile in piles:
            answer += math.ceil(pile / k)
        return answer

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        sum_of_piles = sum(piles)
        len_of_piles = len(piles)

        left = math.ceil(sum_of_piles / h)
        right = math.ceil((sum_of_piles - len_of_piles + 1) / (h - len_of_piles + 1))

        while left < right:
            mid = left + (right - left) // 2

            need_hour = self.getNeedHour(piles, mid)
            if need_hour > h:
                left = mid + 1
            else:
                right = mid

        return left


if __name__ == "__main__":
    print(Solution().minEatingSpeed(piles=[3, 6, 7, 11], h=8))
    print(Solution().minEatingSpeed(piles=[30, 11, 23, 4, 20], h=5))
    print(Solution().minEatingSpeed(piles=[30, 11, 23, 4, 20], h=6))
    print(Solution().minEatingSpeed(piles=[2, 2], h=2))
