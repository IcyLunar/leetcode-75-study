class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        l, r = 0, 0
        cur_zero_cnt = 1 - nums[0]

        answer = 0
        while True:
            if cur_zero_cnt > 1:
                l += 1
                cur_zero_cnt -= 1 - nums[l - 1]
                if l > r:
                    r += 1
                    if r == len(nums):
                        break
                    cur_zero_cnt += 1 - nums[r]

            else:
                answer = max(answer, r - l + 1)

                r += 1
                if r == len(nums):
                    break
                cur_zero_cnt += 1 - nums[r]

        return answer - 1


if __name__ == "__main__":
    print(Solution().longestSubarray(nums=[1, 1, 0, 1]))
    print(Solution().longestSubarray(nums=[0, 1, 1, 1, 0, 1, 1, 0, 1]))
    print(Solution().longestSubarray(nums=[1, 1, 1]))
