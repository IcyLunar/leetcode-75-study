class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = [1 for i in range(len(nums))]

        i, j = 1, len(nums) - 2
        acc1, acc2 = 1, 1
        while i < len(nums):
            acc1 *= nums[i - 1]
            acc2 *= nums[j + 1]

            answer[i] *= acc1
            answer[j] *= acc2

            i += 1
            j -= 1

        return answer


print(Solution().productExceptSelf([1, 2, 3, 4]))
print(Solution().productExceptSelf([-1, 1, 0, -3, 3]))
