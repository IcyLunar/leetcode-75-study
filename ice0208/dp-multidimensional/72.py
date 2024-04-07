# LCS... 복습할 필요가 있음


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for i in range(len(word2) + 1)] for j in range(len(word1) + 1)]

        for i in range(len(word1) + 1):
            j = len(word2)

            dp[i][j] = len(word1) - i

        for j in range(len(word2) + 1):
            i = len(word1)

            dp[i][j] = len(word2) - j

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = min(dp[i + 1][j + 1], dp[i + 1][j], dp[i][j + 1]) + 1

        return dp[0][0]


if __name__ == "__main__":
    print(Solution().minDistance(word1="horse", word2="ros"))
    print(Solution().minDistance(word1="intention", word2="execution"))
