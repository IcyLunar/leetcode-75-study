# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    pass


class Solution:
    def bs(self, l: int, r: int) -> int:
        mid = (r - l) // 2 + l
        print(mid)
        result = guess(mid)

        if result == 0:
            return mid
        elif result == -1:
            return self.bs(l, mid - 1)
        else:
            return self.bs(mid + 1, r)

    def guessNumber(self, n: int) -> int:
        answer = self.bs(1, n)
        return answer
