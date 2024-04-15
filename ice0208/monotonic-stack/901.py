# 스택을 활용한 문제


class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        cur_price, cur_span = price, 1

        while len(self.stack) and self.stack[-1][0] <= cur_price:
            prev_price, prev_span = self.stack.pop()
            cur_span += prev_span

        self.stack.append((cur_price, cur_span))
        return cur_span
