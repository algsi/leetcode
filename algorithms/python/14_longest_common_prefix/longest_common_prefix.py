"""
14. longest common prefix

14. 最长公共前缀
"""

from typing import List


def longest_common_prefix_1(strs: List[str]) -> str:
    """
    纵向扫描

    时间复杂度：O(mn)
    空间复杂度：O(1)
    """
    if not strs:
        return ""

    cursor = 0
    running = True
    while True:
        if not strs[0] or cursor >= len(strs[0]):
            break
        tmp = strs[0][cursor]
        for s in strs[1:]:
            if not s or cursor >= len(s) or s[cursor] != tmp:
                running = False
                break
        if not running:
            break
        cursor += 1

    if not cursor:
        return ""
    return strs[0][:cursor]


if __name__ == '__main__':
    param = ["flower", "flow", "flight"]
    res = longest_common_prefix_1(param)
    print(res)
