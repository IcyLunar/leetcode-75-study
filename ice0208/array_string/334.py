class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        a, b = 2**31 - 1, 2**31 - 1

        for num in nums:
            if num <= a:
                a = num
                continue
            elif num <= b:
                b = num
                continue
            else:
                return True

        return False


if __name__ == "__main__":
    print(Solution().increasingTriplet([1, 2, 3, 4, 5]))
    print(Solution().increasingTriplet([5, 4, 3, 2, 1]))
    print(Solution().increasingTriplet([2, 1, 5, 0, 4, 6]))
    print(Solution().increasingTriplet([20, 100, 10, 12, 5, 13]))
    print(Solution().increasingTriplet([0, 4, 2, 1, 0, -1, -3]))
