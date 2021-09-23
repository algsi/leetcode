"""
415. add strings

https://leetcode.com/problems/add-strings/
https://leetcode-cn.com/problems/add-strings/

字符串相加（大整数相加）
"""


def add_string(num1: str, num2: str) -> str:
    res = ""

    # 两个指针，从右往左移动
    # 进位记录
    i, j, carry = len(num1) - 1, len(num2) - 1, 0
    while i >= 0 or j >= 0:
        n1 = int(num1[i]) if i >= 0 else 0
        n2 = int(num2[j]) if j >= 0 else 0
        tmp = n1 + n2 + carry
        carry = 0 if tmp < 10 else 1
        res = str(tmp % 10) + res  # 注意前后顺序
        i, j = i - 1, j - 1

    # 1 必须放在前面，否则字符串的顺序不对
    return '1' + res if carry else res
