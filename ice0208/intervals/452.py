# 그리드를 이용한 풀이이다.
# 이 문제도 증명을 할 필요가 있다.


class Arrow:
    def __init__(self, start, end):
        self.area_start = start
        self.area_end = end

    def is_overlapping(self, start, end):
        if self.area_start <= start <= self.area_end:
            return True
        if self.area_start <= end <= self.area_end:
            return True
        return False

    def reset_area(self, start, end):
        self.area_start = max(self.area_start, start)
        self.area_end = min(self.area_end, end)


class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        arrows: list[Arrow] = []
        cur_arrow = Arrow(2**31 * -1, 2**31)
        arrows.append(cur_arrow)

        for point in sorted(points, key=lambda a: a[0]):
            if cur_arrow.is_overlapping(*point):
                cur_arrow.reset_area(*point)
            else:
                # 해당되는 arrow가 없음
                new_arrow = Arrow(*point)
                arrows.append(new_arrow)
                cur_arrow = new_arrow

        return len(arrows)


if __name__ == "__main__":
    print(Solution().findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))
    print(Solution().findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]))
    print(Solution().findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]))
