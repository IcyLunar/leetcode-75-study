class Solution:
    def calcEquation(
        self, equations: list[list[str]], values: list[float], queries: list[list[str]]
    ) -> list[float]:
        d = dict()
        stack = []
        s = set()
        for i, e in enumerate(equations):
            stack.append((equations[i][0], equations[i][1], values[i]))
            stack.append((equations[i][1], equations[i][0], 1 / values[i]))

        while stack:
            a, b, r = stack.pop()
            s.add(a)
            s.add(b)
            if (a, b) in d:
                continue
            d[(a, b)] = r

            for key, value in d.items():
                d_a, d_b = key
                if a == d_b and b != d_a:
                    if (d_a, b) not in d:
                        stack.append((d_a, b, r * value))
                        stack.append((b, d_a, 1 / (r * value)))
                elif b == d_a and a != d_b:
                    if (a, d_b) not in d:
                        stack.append((a, d_b, r * value))
                        stack.append((d_b, a, 1 / (r * value)))

        answer = []
        for query in queries:
            a, b = query
            if (a, b) in d:
                answer.append(d[(a, b)])
            elif a == b and a in s:
                answer.append(1.0)
            else:
                answer.append(-1.0)

        return answer


if __name__ == "__main__":
    print(
        Solution().calcEquation(
            equations=[["a", "b"], ["b", "c"]],
            values=[2.0, 3.0],
            queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
        )
    )
    print(
        Solution().calcEquation(
            [["a", "b"], ["b", "c"], ["bc", "cd"]],
            values=[1.5, 2.5, 5.0],
            queries=[["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]],
        )
    )
    print(
        Solution().calcEquation(
            equations=[["a", "b"]],
            values=[0.5],
            queries=[["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]],
        )
    )
