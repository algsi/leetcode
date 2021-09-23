"""
476. number complement

数字的补数
"""


def find_complement(num: int) -> int:
    """
    XOR

    异或运算

    5的二进制是：0101，7的二进制是： 0111，它们的抑或为：0010，去掉前导零位即为取反。
    所以，我们的目标就是找到第一个大于 num 且除去符号位其他位都是 1 的数字
    """

    tmp = 1
    while tmp < num:
        tmp = tmp << 1
        tmp += 1
    return tmp ^ num


def find_complement_2(num: int) -> int:
    """
    数学计算

    num 和补数相加，就是满数位 1 的二进制数，即 2**(n-1)-1
    """
    return 2 ** (len(bin(num)) - 2) - 1 - num
