"""
225. implement stack using queues

用队列实现栈
"""


class MyStack:
    """
    一个队列实现栈

    时间复杂度
    入队：O(n)
    出队：O(1)
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        # 元素入队列后，将队尾元素的前面所有元素都出队并再依次入队
        self.q.append(x)

        n = len(self.q)
        for _ in range(n - 1):
            # 反转前n-1个元素，栈顶元素始终保留在队首
            self.q.append(self.q.pop(0))

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.empty():
            return
        return self.q.pop(0)

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.empty():
            return
        return self.q[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q) == 0
