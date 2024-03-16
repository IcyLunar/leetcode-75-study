class Solution:
    def bs(self, l, r, lst, spell, target):
        mid = (r - l) // 2 + l

        if lst[mid] * spell < target:
            l = mid + 1
        elif lst[mid] * spell >= target:
            r = mid

        if l == r:
            if lst[l] * spell >= target:
                return l
            else:
                return -1

        return self.bs(l, r, lst, spell, target)

    def successfulPairs(
        self, spells: list[int], potions: list[int], success: int
    ) -> list[int]:

        potions.sort()
        answer = []
        for spell in spells:
            min_index = self.bs(0, len(potions) - 1, potions, spell, success)
            if min_index != -1:
                answer.append(len(potions) - min_index)
            else:
                answer.append(0)

        return answer


if __name__ == "__main__":

    print(Solution().successfulPairs(spells=[3, 1, 2], potions=[8, 5, 8], success=16))
