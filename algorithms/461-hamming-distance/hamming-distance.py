"""
461. hamming distance

https://leetcode.com/problems/hamming-distance/
https://leetcode-cn.com/problems/hamming-distance/

汉明距离
"""


def hamming_distance_1(x: int, y: int) -> int:
    """
    语言的内置位计数功能

    Java: Integer.bitCount(x ^ y);
    """
    return bin(x ^ y).count('1')


def hamming_distance_2(x: int, y: int) -> int:
    """
    移位操作：逐位移动，逐位比较边缘位置是否为 1
    """
    tmp = x ^ y
    distance = 0
    while tmp != 0:
        # AND 运算
        if tmp & 1 == 1:
            distance += 1
        tmp = tmp >> 1
    return distance


def hamming_distance_3(x: int, y: int) -> int:
    """
    布赖恩·克尼根算法：在移位操作的基础上，我们发现，如果异或的结果存在非常多的0而只有少量的1，这样我们就花了大量时间找出1的位数。
    寻找一种更快的方法找出等于 1 的位数。

    当我们在 number 和 number-1 上做 AND 位运算时，原数字 number 的最右边等于 1 的比特会被移除。

    https://leetcode-cn.com/problems/hamming-distance/solution/yi-ming-ju-chi-by-leetcode/
    """
    xor = x ^ y
    distance = 0
    while xor:
        distance += 1
        # remove the rightmost bit of '1'
        xor = xor & (xor - 1)
    return distance
