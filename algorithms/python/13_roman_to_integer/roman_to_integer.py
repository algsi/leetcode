"""
13. roman to integer

https://leetcode.com/problems/roman-to-integer/
https://leetcode-cn.com/problems/roman-to-integer/

罗马数字转整数
"""

SYMBOL_VALUES = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


def roman_to_integer(s: str) -> int:
    ans = 0
    n = len(s)
    for i, ch in enumerate(s):
        value = SYMBOL_VALUES[ch]
        if i < n - 1 and value < Solution.SYMBOL_VALUES[s[i + 1]]:
            ans -= value
        else:
            ans += value

    return ans
