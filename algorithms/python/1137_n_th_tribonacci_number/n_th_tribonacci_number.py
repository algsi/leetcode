"""
n th tribonacci number

第 N 个泰波那契数
"""


def tribonacci(n: int) -> int:
    if n == 0:
        return 0
    if n <= 2:
        return 1
    p, q, r, s = 0, 0, 1, 1
    for i in range(3, n + 1):
        p = q
        q = r
        r = s
        s = p + q + r
    return s
