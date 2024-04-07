class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        answer = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while len(stack) > 0 and stack[-1][1] < temp:
                poped_index, poped_temp = stack.pop()
                answer[poped_index] = i - poped_index

            stack.append((i, temp))

        return answer


if __name__ == "__main__":
    print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    print(Solution().dailyTemperatures([30, 40, 50, 60]))
    print(Solution().dailyTemperatures([30, 60, 90]))
