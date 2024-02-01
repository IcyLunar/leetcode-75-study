class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        cnt = 0
        flowerbed = [0, *flowerbed, 0]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 1:
                continue

            if 0 == flowerbed[i - 1] == flowerbed[i + 1]:
                flowerbed[i] = 1
                cnt += 1

        return cnt >= n


if __name__ == "__main__":
    print(Solution().canPlaceFlowers([1, 0, 0, 0, 1], 1))
    print(Solution().canPlaceFlowers([1, 0, 0, 0, 1], 2))
