class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        # return할 변수
        answer = [False for _ in range(len(candies))]
        # kid가 가지고 있는 최대 사탕의 개수
        max_of_candies = max(candies)

        # 각 kid 마다 extraCandies를 더한 리스트
        candies2 = [(candy + extraCandies) for candy in candies]

        # candies2가 max_of_candies보다 크거나 같을 때 해당 kid의 answer를 True로 변경
        for i in range(len(answer)):
            if candies2[i] >= max_of_candies:
                answer[i] = True

        return answer


if __name__ == "__main__":
    print(Solution().kidsWithCandies([2, 3, 5, 1, 3], 3))
    print(Solution().kidsWithCandies([4, 2, 1, 1, 2], 1))
    print(Solution().kidsWithCandies([12, 1, 12], 10))
