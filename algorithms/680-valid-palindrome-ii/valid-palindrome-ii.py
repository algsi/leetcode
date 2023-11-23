"""
680. valid palindrome ii

https://leetcode-cn.com/problems/valid-palindrome-ii/
https://leetcode.com/problems/valid-palindrome-ii/

验证回文字符串 Ⅱ
"""


def valid_palindrome(s: str) -> bool:
    if len(s) == 1:
        return True
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            break
        left += 1
        right -= 1

    if left < right:
        # 遇到不等的情况，尝试删除左字符或右字符
        return valid_palindrome_internal(s, left + 1, right) or valid_palindrome_internal(s, left, right - 1)
    else:
        return True


def valid_palindrome_internal(s: str, left: int, right: int) -> bool:
    if left == right:
        return True
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True
