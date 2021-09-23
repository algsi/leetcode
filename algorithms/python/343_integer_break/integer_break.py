"""
343. integer break

https://leetcode-cn.com/problems/integer-break/
https://leetcode-cn.com/problems/jian-sheng-zi-lcof/

整数拆分（剪绳子）
"""

import math


def integer_break(n: int) -> int:
    """
    数学推导
    """
    if n <= 3:
        return n - 1

    a, b = n // 3, n % 3
    if b == 0:
        return int(math.pow(3, a))
    if b == 1:
        return int(math.pow(3, a - 1) * 4)
    return int(math.pow(3, a) * 2)
