"""
171. excel sheet column number

https://leetcode.com/problems/excel-sheet-column-number/
https://leetcode-cn.com/problems/excel-sheet-column-number/

Excel 表列序号
"""


def title_to_number(column_title: str) -> int:
    """
    26 进制
    """
    if not column_title:
        return 0
    tmp = 1
    base = ord('A')
    ret = 0
    for c in column_title[::-1]:
        ret += (ord(c) - base + 1) * tmp
        tmp *= 26
    return ret
