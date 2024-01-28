class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        check = 0
        i = 0
        while check < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
            else:
                i += 1

            check += 1

        return nums


if __name__ == "__main__":
    print(Solution().moveZeroes([0, 1, 0, 3, 12]))
    print(Solution().moveZeroes([0]))
