class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        not_visit = set(range(0, len(rooms)))

        stack = [0]

        while stack:
            cur = stack.pop()
            if cur in not_visit:
                not_visit.remove(cur)
                stack.extend(rooms[cur])

        return not not_visit
