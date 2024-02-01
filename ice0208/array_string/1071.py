class Solution:
    def isDivisor(self, s: str, t: str, step: int) -> bool:
        for i in range(0, len(s), step):
            if s[i : i + step] != t:
                return False
        return True

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            str1, str2 = str2, str1

        for step in range(len(str1) + 1, 0, -1):
            cur_t = str1[0:step]

            if self.isDivisor(str1, cur_t, step):
                if self.isDivisor(str2, cur_t, step):
                    return cur_t

        return ""


if __name__ == "__main__":
    print(Solution().gcdOfStrings("ABCABC", "ABC"))  # "ABC"
    print(Solution().gcdOfStrings("ABABAB", "ABAB"))  # "AB"
    print(Solution().gcdOfStrings("LEET", "CODE"))  # ""
