class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # return할 문자열
        answer = ""

        # 같은 index끼리 순서대로 merge
        for w1, w2 in zip(word1, word2):
            answer += f"{w1}{w2}"

        # 남은 부분 합치기
        word_min_len = min(len(word1), len(word2))
        answer += word1[word_min_len:] + word2[word_min_len:]

        return answer


if __name__ == "__main__":
    print(Solution().mergeAlternately("abc", "pqr"))  # apbqcr
    print(Solution().mergeAlternately("ab", "pqrs"))  # apbqrs
    print(Solution().mergeAlternately("abcd", "pq"))  # apbqcd
