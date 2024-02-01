class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # 슬라이딩 방식을 이용하여 O(n)의 시간복잡도로 해결

        l, r = 0, k - 1

        current_range_sum = sum(nums[l : r + 1])
        max_range_sum = -(10**9)

        while True:
            max_range_sum = max(max_range_sum, current_range_sum)
            l += 1
            r += 1
            if r == len(nums):
                break

            current_range_sum -= nums[l - 1]
            current_range_sum += nums[r]

        return max_range_sum / k


if __name__ == "__main__":
    print(Solution().findMaxAverage(nums=[1, 12, -5, -6, 50, 3], k=4))
    print(Solution().findMaxAverage(nums=[5], k=1))
