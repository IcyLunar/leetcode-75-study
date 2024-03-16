from heapq import heapify, heappop, heappush
from collections import deque

# 정렬로 풀이 -> 시간 초과 -> heapq를 이용한 풀이 -> len(costs)가 candidate*2보다 작은 경우를 생각안해서 틀림
# -> 다시 수정 -> 겨우 정답
# 난이도: (3.7/5)


class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:

        if len(costs) >= candidates * 2:
            target_area = [
                *[
                    (v, i, False)
                    for v, i in zip(costs[:candidates], range(0, candidates))
                ],
                *[
                    (v, i, True)
                    for v, i in zip(
                        costs[-candidates:], range(len(costs) - candidates, len(costs))
                    )
                ],
            ]
            remain_area = deque(
                [
                    (v, i)
                    for v, i in zip(
                        [*costs[candidates:-candidates]],
                        range(candidates, len(costs) - candidates),
                    )
                ]
            )
        else:
            target_area = [
                *[(v, i, False) for v, i in zip(costs, range(0, len(costs)))],
            ]
            remain_area = deque([])

        heapify(target_area)
        answer = 0

        for _ in range(k):
            cur_v, cur_i, cur_isright = heappop(target_area)

            if remain_area:
                if cur_isright:
                    heappush(target_area, (*remain_area.pop(), True))
                else:
                    heappush(target_area, (*remain_area.popleft(), False))

            answer += cur_v

        return answer
