"""
49. group anagrams

https://leetcode.com/problems/group-anagrams/
https://leetcode-cn.com/problems/group-anagrams/

字母异位词分组
"""

from typing import List
import collections


class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        map = collections.defaultdict(list)
        for st in strs:
            counts = [0] * 26
            for ch in st:
                counts[ord(ch) - ord('a')] += 1
            # 需要将 list 转换成 tuple 才能进行哈希
            map[tuple(counts)].append(st)
        return list(map.values())
