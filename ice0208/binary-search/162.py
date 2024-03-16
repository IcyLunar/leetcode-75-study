# O(n)으로는 금방 풀었는데 binary search로 어떻게 풀지 생각이 나지 않았다.
# Solutions를 보고 힌트를 얻고 풀었다.


class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        length = len(nums)

        l, r = 0, length - 1

        while l <= r:
            mid = (r - l) // 2 + l

            if mid != length - 1 and nums[mid] < nums[mid + 1]:
                l = mid + 1
            elif mid != 0 and nums[mid] < nums[mid - 1]:
                r = mid - 1
            else:
                return mid
