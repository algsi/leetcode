"""
214. shortest palindrome

最短回文串
"""


def shortest_palindrome(s: str) -> str:
    """
    字符串哈希

    找到字符串的最长前缀回文串
    """
    n = len(s)
    base, mod = 131, 10 ** 9 + 7
    left = right = 0
    mul = 1
    best = -1

    for i in range(n):
        left = (left * base + ord(s[i])) % mod
        right = (right + mul * ord(s[i])) % mod
        if left == right:
            best = i
        mul = mul * base % mod

    add = ("" if best == n - 1 else s[best + 1:])
    return add[::-1] + s
