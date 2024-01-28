class Solution:
    def compress(self, chars: list[str]) -> int:
        answer = 0
        new_chars = []

        before = None
        cnt = 0
        for char in chars:
            if before == None:
                cnt += 1
                before = char
                new_chars.append(char)
                continue

            if before == char:
                cnt += 1
            else:
                if cnt == 1:
                    answer += 1
                else:
                    answer += 1
                    answer += cnt // 10 + 1
                    new_chars.extend(list(str(cnt)))

                before = char
                new_chars.append(char)
                cnt = 1

        if cnt == 1:
            answer += 1
        else:
            answer += 1
            answer += cnt // 10 + 1
            new_chars.extend(list(str(cnt)))

        chars.clear()
        chars.extend(new_chars)
        return answer


if __name__ == "__main__":
    print(Solution().compress(["a", "a", "b", "b", "c", "c", "c"]))
    print(Solution().compress(["a"]))
    print(
        Solution().compress(
            ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
        )
    )
