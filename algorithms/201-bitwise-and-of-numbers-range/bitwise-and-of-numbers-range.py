"""
201. bitwise and of numbers range

https://leetcode.com/problems/bitwise-and-of-numbers-range
https://leetcode-cn.com/problems/bitwise-and-of-numbers-range

数字范围按位与
"""


def range_bitwise_and_1(m: int, n: int) -> int:
    """
    Brian Kernighan 算法：找出二进制的公共前缀

    参考 461 题：汉明距离
    """
    while m < n:
        # # 抹去最右边的 1
        n = n & (n - 1)
    return n
