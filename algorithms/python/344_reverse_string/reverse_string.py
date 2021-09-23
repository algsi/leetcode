"""
344. reverse string
"""

from typing import List


def reverse_string(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    if not s:
        return

    n = len(s)
    lo, hi = 0, n - 1
    while lo < hi:
        s[lo], s[hi] = s[hi], s[lo]
        lo += 1
        hi -= 1
