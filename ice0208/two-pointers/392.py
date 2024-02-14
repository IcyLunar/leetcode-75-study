class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        i = 0
        max_i = len(s) - 1

        for tt in t:
            if s[i] == tt:
                i += 1
                if i > max_i:
                    return True

        return False


if __name__ == "__main__":
    print(Solution().isSubsequence(s="abc", t="ahbgdc"))  # True
    print(Solution().isSubsequence(s="axc", t="ahbgdc"))  # False
