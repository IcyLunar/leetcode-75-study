import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.back_list = []
        self.back_set = set()
        self.last = 1

    def popSmallest(self) -> int:
        if self.back_list:
            answer = heapq.heappop(self.back_list)
            self.back_set.remove(answer)
            return answer
        else:
            answer = self.last
            self.last += 1
            return answer

    def addBack(self, num: int) -> None:
        if num < self.last and num not in self.back_set:
            heapq.heappush(self.back_list, num)
            self.back_set.add(num)
