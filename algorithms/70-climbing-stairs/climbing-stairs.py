"""
70. climbing stairs

爬楼梯（青蛙跳台阶）
"""


def climb_stairs(n: int) -> int:
    """
    DP
    当 n=1，f(1)=1
    当 n=2，f(2)=2
    当 n>2，f(n)=f(n-1)+f(n-2)

    实际上这是一个斐波那契数列。因为我们只用到了前两个状态，所有也就没必要使用数组来保存前面所有的状态了
    """
    if n == 1:
        return 1
    if n == 2:
        return 2

    f1, f2 = 1, 2
    for _ in range(3, n + 1):
        f1, f2 = f2, f1 + f2

    return f2
