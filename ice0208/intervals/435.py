# 간격 스케줄링 문제, 증명에 대하여 살펴볼 필요가 있다.


class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        interval_list = [False] * 10**5

        def is_overlapping(start, end):
            for cur in range(start, end):
                if interval_list[cur] == True:
                    return True
            return False

        def add_interval(start, end):
            for cur in range(start, end):
                interval_list[cur] = True

        answer = 0
        for interval in sorted(intervals, key=lambda a: a[1]):
            if is_overlapping(*interval):
                answer += 1
            else:
                add_interval(*interval)

        return answer


if __name__ == "__main__":
    print(Solution().eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
    print(Solution().eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))
    print(Solution().eraseOverlapIntervals([[1, 2], [2, 3]]))
