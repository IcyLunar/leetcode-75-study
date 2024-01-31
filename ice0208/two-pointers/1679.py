class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        # 요약: 정렬 후 투 포인터

        # nums를 정렬합니다.
        nums.sort()

        # left와 right포인터를 초기 세팅합니다.
        left, right = 0, len(nums) - 1

        # left와 right 사이의 범위를 서서히 줄입니다.
        # 범위를 줄이면서 left와 right 대상의 합이 k이면 count를 셉니다.
        count = 0
        while left < right:
            cur_sum = nums[left] + nums[right]

            if cur_sum == k:
                count += 1
                left += 1
                right -= 1

            elif cur_sum > k:
                right -= 1
            else:
                left += 1

        return count


if __name__ == "__main__":
    print(Solution().maxOperations(nums=[1, 2, 3, 4], k=5))
    print(Solution().maxOperations(nums=[3, 1, 3, 4, 3], k=6))
