class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        if sorted(word1) == sorted(word2):
            return True

        d1 = dict()
        for w in word1:
            d1[w] = d1.get(w, 0) + 1

        d2 = dict()
        for w in word2:
            d2[w] = d2.get(w, 0) + 1

        if sorted(d1.keys()) == sorted(d2.keys()) and sorted(d1.values()) == sorted(
            d2.values()
        ):
            return True

        return False


if __name__ == "__main__":
    print(Solution().closeStrings(word1="abc", word2="bca"))
    print(Solution().closeStrings(word1="a", word2="aa"))
    print(Solution().closeStrings(word1="cabbba", word2="abbccc"))
