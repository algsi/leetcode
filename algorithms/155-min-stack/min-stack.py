"""
155. min stack

最小栈
"""


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack_a = []
        self.stack_b = []  # 辅助栈，栈中存最小元素的索引

    def push(self, x: int) -> None:
        if len(self.stack_a) == 0 or self.getMin() > x:
            self.stack_b.append(len(self.stack_a))
        self.stack_a.append(x)

    def pop(self) -> None:
        if len(self.stack_a) == 0:
            raise IndexError('pop from empty stack')
        if self.stack_b[-1] == len(self.stack_a) - 1:
            self.stack_b.pop()
        return self.stack_a.pop()

    def top(self) -> int:
        if len(self.stack_a) == 0:
            raise IndexError('top from empty stack')
        return self.stack_a[-1]

    def getMin(self) -> int:
        if len(self.stack_a) == 0:
            raise IndexError('get min from empty stack')
        return self.stack_a[self.stack_b[-1]]
