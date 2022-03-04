"""
排列硬币
"""


def arrange_coins(n: int) -> int:
    """
    二分查找
    n 个硬币至少可以组成 1 个完整阶梯行，至多可以组成 n 个完整阶梯行
    """
    left, right = 1, n
    while left < right:
        mid = (right + left + 1) // 2
        if mid * (mid + 1) <= 2 * n:
            # 当一直出现 left = mid 时可能会进入死循环，因此 mid 在偶数个数时应该取右边的数字
            left = mid
        else:
            right = mid - 1
    return left
