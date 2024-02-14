class Solution:
    VOWEL_SET = {"a", "e", "i", "o", "u"}

    def maxVowels(self, s: str, k: int) -> int:
        # 643 문제와 같은 슬라이딩 방식으로 쉽게 해결 가능

        k_range_vowel_cnt = 0
        for i in range(0, k):
            if s[i] in Solution.VOWEL_SET:
                k_range_vowel_cnt += 1

        max_range_vowel_cnt = k_range_vowel_cnt
        for r in range(k, len(s)):
            l = r - k + 1
            if s[l - 1] in Solution.VOWEL_SET:
                k_range_vowel_cnt -= 1
            if s[r] in Solution.VOWEL_SET:
                k_range_vowel_cnt += 1

            max_range_vowel_cnt = max(max_range_vowel_cnt, k_range_vowel_cnt)

        return max_range_vowel_cnt


if __name__ == "__main__":
    print(Solution().maxVowels(s="abciiidef", k=3))
    print(Solution().maxVowels(s="aeiou", k=2))
    print(Solution().maxVowels(s="leetcode", k=3))
