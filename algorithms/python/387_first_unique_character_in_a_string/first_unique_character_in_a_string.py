"""
387. first unique character in a string

https://leetcode.com/problems/first-unique-character-in-a-string/
https://leetcode-cn.com/problems/first-unique-character-in-a-string/

字符串中的第一个唯一字符
"""

import collections


class Solution:
    """
    哈希表
    """

    def first_uniq_char(self, s: str) -> int:
        frequency = collections.Counter(s)
        for idx, ch in enumerate(s):
            if frequency[ch] == 1:
                return idx
        return -1
