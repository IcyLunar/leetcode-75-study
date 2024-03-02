from collections import deque


class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:

        len_r, len_c = len(maze), len(maze[0])

        moves = ((0, 1), (0, -1), (1, 0), (-1, 0))
        visit = [[False for _ in range(len_c)] for __ in range(len_r)]

        q = deque()
        q.append((entrance[0], entrance[1], 0))
        visit[entrance[0]][entrance[1]] = True

        while q:
            cur_r, cur_c, cnt = q.popleft()

            for move in moves:
                nxt_r = cur_r + move[0]
                nxt_c = cur_c + move[1]

                if not (0 <= nxt_r < len_r) or not (0 <= nxt_c < len_c):
                    if cnt > 0:
                        return cnt
                    continue

                if maze[nxt_r][nxt_c] == "+":
                    continue

                if visit[nxt_r][nxt_c]:
                    continue
                visit[nxt_r][nxt_c] = True
                q.append((nxt_r, nxt_c, cnt + 1))

        return -1
