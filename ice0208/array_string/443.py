class Solution:
    def compress(self, chars: list[str]) -> int:
        before = chars[-1]
        cnt = 1
        s, e = len(chars) - 1, len(chars) - 1
        for i in range(len(chars) - 2, -1, -1):
            if chars[i] == before:
                cnt += 1
                s -= 1
            else:
                del chars[s + 1 : e + 1]
                if cnt > 1:
                    for cc in reversed(list(str(cnt))):
                        chars.insert(s + 1, cc)

                before = chars[i]
                cnt = 1
                s, e = i, i

        del chars[s + 1 : e + 1]
        if cnt > 1:
            for cc in reversed(list(str(cnt))):
                chars.insert(s + 1, cc)

        return len(chars)


if __name__ == "__main__":
    print(Solution().compress(["a", "a", "b", "b", "c", "c", "c"]))
    print(Solution().compress(["a"]))
    print(
        Solution().compress(
            ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
        )
    )
