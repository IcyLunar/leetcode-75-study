class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        map = dict()
        for num in arr:
            map[num] = map.get(num, 0) + 1

        cnt_set = set()
        for k, v in map.items():
            cnt_set.add(v)

        return len(map) == len(cnt_set)


if __name__ == "__main__":
    print(Solution().uniqueOccurrences(arr=[1, 2, 2, 1, 1, 3]))
    print(Solution().uniqueOccurrences(arr=[1, 2]))
    print(Solution().uniqueOccurrences(arr=[-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))
