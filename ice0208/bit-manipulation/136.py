# 비트 조작 유형이라는 것을 몰랐으면 쉽게 풀 수 있었을까


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        answer = 0

        for num in nums:
            answer = answer ^ num
        return answer


if __name__ == "__main__":
    print(Solution().singleNumber(nums=[2, 2, 1]))
    print(Solution().singleNumber(nums=[4, 1, 2, 1, 2]))
    print(Solution().singleNumber(nums=[1]))
