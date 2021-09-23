"""
409. longest palindrome

最长回文串
"""


def longest_palindrome(s: str) -> int:
    if not s:
        return 0

    num_count = [0] * 128
    for i in s:
        num_count[ord(i)] += 1

    # 奇数数量的字符
    count = 0
    for i in num_count:
        count += (i % 2)

    # 在一个回文串中，只有最多一个字符出现了奇数次，其余的字符都出现偶数次。
    return len(s) if count == 0 else len(s) - count + 1
