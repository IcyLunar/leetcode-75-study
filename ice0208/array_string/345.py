class Solution:
    def reverseVowels(self, s: str) -> str:
        VOWELS = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        l, r = 0, len(s) - 1
        s_list = list(s)

        while l < r:
            if s_list[l] not in VOWELS:
                l += 1
                continue
            if s_list[r] not in VOWELS:
                r -= 1
                continue

            s_list[l], s_list[r] = s_list[r], s_list[l]
            l += 1
            r -= 1

        return "".join(s_list)


if __name__ == "__main__":
    print(Solution().reverseVowels("hello"))  # "holle"
    print(Solution().reverseVowels("leetcode"))  # "leotcede"
