class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                self.collide(stack, a)

        return stack

    def collide(self, stack, a):
        while True:
            if len(stack) == 0:
                stack.append(a)
                return
            elif stack[-1] < 0:
                stack.append(a)
                return
            else:
                if stack[-1] == -a:
                    stack.pop()
                    return
                elif stack[-1] < -a:
                    stack.pop()
                else:
                    return


if __name__ == "__main__":

    testcase_list = [[5, 10, -5], [8, -8], [10, 2, -5]]

    for testcase in testcase_list:
        print(Solution().asteroidCollision(asteroids=testcase))
