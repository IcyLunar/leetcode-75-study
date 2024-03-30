# 비트 연산자에 익숙해질 필요가 있음


class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0]

        for i in range(1, n + 1):
            ans.append(ans[i >> 1] + (i & 1))

        return ans


if __name__ == "__main__":
    print(Solution().countBits(2))
    print(Solution().countBits(8))
