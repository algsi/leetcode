"""
1047. remove all adjacent duplicates in string

https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string/

删除字符串中的所有相邻重复项
"""


def remove_duplicates(S: str) -> str:
    stk = list()
    for ch in S:
        if stk and stk[-1] == ch:
            stk.pop()
        else:
            stk.append(ch)
    return ''.join(stk)
