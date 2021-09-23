"""
541. reverse string II

https://leetcode.com/problems/reverse-string-ii/
https://leetcode-cn.com/problems/reverse-string-ii/

反转字符串 II
"""


def reverse_str(s: str, k: int) -> str:
    t = list(s)
    for i in range(0, len(t), 2 * k):
        t[i: i + k] = reversed(t[i: i + k])
    return ''.join(t)
