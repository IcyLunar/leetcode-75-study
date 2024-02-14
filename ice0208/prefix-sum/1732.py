class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        prefix_sum = 0
        max_sum = 0

        for g in gain:
            prefix_sum += g
            max_sum = max(max_sum, prefix_sum)

        return max_sum


if __name__ == "__main__":
    print(Solution().largestAltitude(gain=[-5, 1, 5, 0, -7]))
    print(Solution().largestAltitude(gain=[-4, -3, -2, -1, 4, 3, 2]))
