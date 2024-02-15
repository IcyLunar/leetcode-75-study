class Solution:
    def decodeString(self, s: str) -> str:
        digit_stack = []
        str_stack = []
        answer = ""

        digit_temp = ""
        str_temp = ""

        for c in s:
            if c.isdigit():
                digit_temp += c
                continue
            elif digit_temp:
                digit_stack.append(int(digit_temp))
                digit_temp = ""

            if c not in ("[", "]"):
                str_temp += c
                continue

            if c == "[":
                str_stack.append(str_temp)
                str_temp = ""
            elif c == "]":
                temp = str_temp * digit_stack.pop()
                str_temp = str_stack.pop() + temp

        answer = str_temp
        return answer


if __name__ == "__main__":
    testcase_list = ["3[a]2[bc]", "3[a2[c]]", "2[abc]3[cd]ef"]

    for testcase in testcase_list:
        print(Solution().decodeString(s=testcase))
