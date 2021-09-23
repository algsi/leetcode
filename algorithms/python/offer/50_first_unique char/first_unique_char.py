"""
LeetCode 面试题50. 第一个只出现一次的字符

https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/
"""


def first_uniq_char(s: str) -> str:
    if not s:
        return ''

    dic = {}
    for c in s:
        dic[c] = not c in dic
    for k, v in dic.items():
        if v:
            return k

    return ''
