class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1

        answer = 0
        while l < r:
            w = r - l
            h = min(height[l], height[r])

            answer = max(answer, w * h)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return answer


if __name__ == "__main__":
    print(Solution().maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
    print(Solution().maxArea(height=[1, 1]))  # 1
