class Solution:
    def reverseWords(self, s: str) -> str:
        ss = s.split()
        ss.reverse()

        return " ".join(ss)


if __name__ == "__main__":
    print(Solution().reverseWords("the sky is blue"))
    print(Solution().reverseWords("  hello world  "))
    print(Solution().reverseWords("a good   example"))
