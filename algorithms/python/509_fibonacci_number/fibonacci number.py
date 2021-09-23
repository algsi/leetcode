"""
509. fibonacci number

https://leetcode-cn.com/problems/fibonacci-number/

斐波那契数
"""


class Solution:
    """
    dynamic programming
    """

    def fib(self, n: int) -> int:
        if n < 2:
            return n

        p, q, r = 0, 0, 1
        for i in range(2, n + 1):
            p, q = q, r
            r = p + q

        return r
