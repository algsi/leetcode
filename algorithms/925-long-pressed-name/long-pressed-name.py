"""
925. long pressed name

https://leetcode.com/problems/long-pressed-name/
https://leetcode-cn.com/problems/long-pressed-name/
"""


class Solution:
    """
    双指针
    """

    def isLongPressedName(self, name: str, typed: str) -> bool:
        n1, n2 = len(name), len(typed)
        p1, p2 = 0, 0
        while p2 < n2:
            if p1 < n1 and name[p1] == typed[p2]:
                p1 += 1
                p2 += 1
            elif p2 > 0 and typed[p2 - 1] == typed[p2]:
                p2 += 1
            else:
                return False
        return p1 == n1
