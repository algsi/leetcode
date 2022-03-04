"""
232. implement queue using stacks

用栈实现队列
"""


class MyQueue:
    """
    两个栈实现队列

    时间复杂度
    入队：O(1)
    出队：均摊复杂度O(1)
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.A = []
        self.B = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.A.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty():
            return

        # data migration
        if len(self.B) == 0:
            while len(self.A) != 0:
                self.B.append(self.A.pop())

        return self.B.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """

        if self.empty():
            return

        # data migration
        if len(self.B) == 0:
            while len(self.A) != 0:
                self.B.append(self.A.pop())

        return self.B[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.A) == 0 and len(self.B) == 0:
            return True
        return False
