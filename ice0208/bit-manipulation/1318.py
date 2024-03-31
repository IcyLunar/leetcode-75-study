# 비효율적으로 푼 느낌


class Solution:
    def needFlipNum(self, a, b, c):
        if c == "0":
            cnt = 0
            if a == "1":
                cnt += 1
            if b == "1":
                cnt += 1
            return cnt
        else:
            if a == b == "0":
                return 1
            else:
                return 0

    def minFlips(self, a: int, b: int, c: int) -> int:
        answer = 0
        for (
            b_a,
            b_b,
            b_c,
        ) in zip(
            bin(a)[2:].rjust(50, "0"),
            bin(b)[2:].rjust(50, "0"),
            bin(c)[2:].rjust(50, "0"),
        ):
            answer += self.needFlipNum(b_a, b_b, b_c)
        return answer


if __name__ == "__main__":
    print(Solution().minFlips(2, 6, 5))
    print(Solution().minFlips(4, 2, 7))
    print(Solution().minFlips(1, 2, 3))
