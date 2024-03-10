from heapq import heapify, heappop


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heapify(nums)
        for _ in range(len(nums) - k):
            heappop(nums)
        return heappop(nums)
