class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left_sum_prefixs = [0]
        for num in nums[:-1]:
            left_sum_prefixs.append(left_sum_prefixs[-1] + num)

        right_sum_prefixs = [0]
        for num in nums[:0:-1]:
            right_sum_prefixs.append(right_sum_prefixs[-1] + num)
        right_sum_prefixs.reverse()

        for i in range(len(nums)):
            if left_sum_prefixs[i] == right_sum_prefixs[i]:
                return i
        return -1


if __name__ == "__main__":
    print(Solution().pivotIndex(nums=[1, 7, 3, 6, 5, 6]))
    print(Solution().pivotIndex(nums=[1, 2, 3]))
    print(Solution().pivotIndex(nums=[2, 1, -1]))
