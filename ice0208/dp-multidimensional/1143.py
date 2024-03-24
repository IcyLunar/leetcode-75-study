# 힌트를 이용하여 풀었습니다.
# 푼 후에 관련 영상을 시청했습니다.
# https://www.youtube.com/watch?v=ASoaQq66foQ
# https://www.youtube.com/watch?v=Ua0GhsJSlWM


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[len(text1)][len(text2)]


if __name__ == "__main__":
    print(Solution().longestCommonSubsequence("abcde", "ace"))
    print(Solution().longestCommonSubsequence("abc", "abc"))
    print(Solution().longestCommonSubsequence("abc", "def"))
