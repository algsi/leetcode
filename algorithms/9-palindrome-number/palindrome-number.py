"""
9. palindrome number

回文数
"""


def is_palindrome(x: int) -> bool:
    """
    转换成字符串
    """
    s = str(x)
    if not s:
        return True
    lo, hi = 0, len(s) - 1
    while lo < hi:
        if s[lo] != s[hi]:
            return False
        lo += 1
        hi -= 1

    return True
