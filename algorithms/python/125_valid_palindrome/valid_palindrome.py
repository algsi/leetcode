"""
125. valid palindrome

验证回文串
"""


def is_palindrome(s: str) -> bool:
    """
    双指针
    """

    left, right = 0, len(s) - 1
    while left < right:
        # 将两个指针都移动到下一个字母或者数字
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if left < right:
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

    return True


if __name__ == '__main__':
    res = is_palindrome('race a car')
    print(res)
