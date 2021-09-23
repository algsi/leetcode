"""
69. sqrtx

https://leetcode.com/problems/sqrtx/
https://leetcode-cn.com/problems/sqrtx/

x 的平方根
"""


def my_sqrt(x: int) -> int:
    """
    二分查找
    """
    if x < 2:
        return x

    lo, hi = 1, x // 2
    ans = -1
    while lo <= hi:
        mid = (hi - lo) // 2 + lo
        tmp = mid ** 2
        if mid ** 2 <= x:
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1

    return ans


def newton(x: int) -> int:
    """
    牛顿法
    """
    if x < 2:
        return x

    x0 = x
    x1 = (x0 + x / x0) / 2
    while abs(x1 - x0) >= 1:
        x0 = x1
        x1 = (x0 + x / x0) / 2

    return int(x1)


if __name__ == '__main__':
    print(newton(156489158))
