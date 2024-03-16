from heapq import heapify, heappop, heappush

# (4/5) 블로그 참고하면서 겨우품 (https://velog.io/@ilov1112/Leetcode-2542.-Maximum-Subsequence-Score)


class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:

        answer = 0
        nums = [(-n2, n2, n1) for n1, n2 in zip(nums1, nums2)]
        heapify(nums)

        heap = []
        n1_sum = 0

        while nums:
            key, nn2, nn1 = heappop(nums)

            if len(heap) > k - 1:
                n1_sum -= heappop(heap)

            n1_sum += nn1
            heappush(heap, nn1)
            if len(heap) == k:
                answer = max(answer, n1_sum * nn2)

        return answer


if __name__ == "__main__":
    testcase_list = [
        {"num1": [1, 3, 3, 2], "num2": [2, 1, 3, 4], "k": 3},
        {"num1": [4, 2, 3, 1, 1], "num2": [7, 5, 10, 9, 6], "k": 1},
    ]

    for testcase in testcase_list:
        print(Solution().maxScore(testcase["num1"], testcase["num2"], testcase["k"]))
