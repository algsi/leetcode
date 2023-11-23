"""
455. assign cookies

https://leetcode.com/problems/assign-cookies/
https://leetcode-cn.com/problems/assign-cookies/

分发饼干
"""

from typing import List


class Solution:
    """
    排序 + 贪心
    """

    def find_content_children(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        result = 0
        j = 0
        len_s = len(s)
        for i in g:
            while s[j] < i and j < len_s:
                j += 1
            if j >= len_s:
                return result
            else:
                result += 1
                j += 1
        return result
