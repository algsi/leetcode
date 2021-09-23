"""
67. add binary

二进制求和
"""


def add_binary(a: str, b: str) -> str:
    """
    输入: a = "1010", b = "1011"
    输出: "10101"
    """
    ia, ib = len(a) - 1, len(b) - 1
    res = ''
    carry = 0
    while ia >= 0 or ib >= 0:
        n = 0 if ia < 0 else int(a[ia])
        m = 0 if ib < 0 else int(b[ib])
        tmp = n + m + carry
        res = str(tmp % 2) + res
        carry = tmp // 2
        ia -= 1
        ib -= 1

    if carry:
        res = str(carry) + res

    return res


if __name__ == '__main__':
    r = add_binary('11', '1')
    print(r)
