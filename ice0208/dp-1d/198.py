class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        nums[2] += nums[0]

        for i in range(3, len(nums)):
            nums[i] = nums[i] + max(nums[i - 2], nums[i - 3])

        return max(nums[-2:])


if __name__ == "__main__":
    print(Solution().rob([1, 2, 3, 1]))
    print(Solution().rob([2, 7, 9, 3, 1]))
