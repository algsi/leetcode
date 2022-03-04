"""
830. positions of large groups

https://leetcode.com/problems/positions-of-large-groups/
https://leetcode-cn.com/problems/positions-of-large-groups/

较大分组的位置
"""

from typing import List


class Solution:
    """
    一次遍历

    time complexity: O(n)
    space complexity: O(1)
    """

    def large_group_positions(self, s: str) -> List[List[int]]:
        prev = 0
        length = len(s)
        output = []
        for i in range(length):
            if s[i] != s[prev]:
                if i - prev >= 3:
                    output.append([prev, i - 1])
                prev = i
        if length - prev >= 3:
            output.append([prev, length - 1])
        return output
