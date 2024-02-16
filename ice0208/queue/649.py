from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q = deque(senate)

        r_cnt = senate.count("R")
        d_cnt = senate.count("D")
        r_ban, d_ban = 0, 0

        while len(q) > 1 and r_cnt and d_cnt:
            if q[0] == "R":
                if r_ban > 0:
                    q.popleft()
                    r_ban -= 1
                    r_cnt -= 1
                    continue
                d_ban += 1
            else:
                if d_ban > 0:
                    q.popleft()
                    d_ban -= 1
                    d_cnt -= 1
                    continue
                r_ban += 1

            q.rotate(-1)  # 왼쪽으로 1칸 이동 rotate

        return "Radiant" if q[0] == "R" else "Dire"


if __name__ == "__main__":
    testcase_list = ["RD", "RDD"]

    for testcase in testcase_list:
        print(Solution().predictPartyVictory(senate=testcase))
