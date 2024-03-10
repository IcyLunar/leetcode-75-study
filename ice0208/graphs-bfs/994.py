from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        moves = ((1, 0), (-1, 0), (0, 1), (0, -1))
        len_r, len_c = len(grid), len(grid[0])

        fresh_cnt = 0
        q = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh_cnt += 1
                elif grid[r][c] == 2:
                    q.append((r, c, 0))
                    grid[r][c] = 0

        min_reseult = 0
        while q:
            cur_r, cur_c, cur_m = q.popleft()
            min_reseult = cur_m

            for move in moves:
                nxt_r, nxt_c = cur_r + move[0], cur_c + move[1]

                if not (0 <= nxt_r < len_r) or not (0 <= nxt_c < len_c):
                    continue

                if grid[nxt_r][nxt_c] == 0:
                    continue

                q.append((nxt_r, nxt_c, cur_m + 1))
                grid[nxt_r][nxt_c] = 0
                fresh_cnt -= 1

        if fresh_cnt == 0:
            return min_reseult
        else:
            return -1
