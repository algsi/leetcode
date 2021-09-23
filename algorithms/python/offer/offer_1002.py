"""
面试题 10.02. 变位词组

https://leetcode-cn.com/problems/group-anagrams-lcci/
"""
import collections
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    排序
    """
    mp = collections.defaultdict(list)
    for st in strs:
        key = ''.join(sorted(st))
        mp[key].append(st)

    return list(mp.values())
