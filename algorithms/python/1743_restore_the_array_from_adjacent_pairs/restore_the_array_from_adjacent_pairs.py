"""
1743. restore the array from adjacent pairs

https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/
https://leetcode-cn.com/problems/restore-the-array-from-adjacent-pairs/

从相邻元素对还原数组
"""

from typing import List
import collections


def restore_array(adjacentPairs: List[List[int]]) -> List[int]:
    """
    哈希表
    """
    mp = collections.defaultdict(list)
    for pair in adjacentPairs:
        mp[pair[0]].append(pair[1])
        mp[pair[1]].append(pair[0])

    n = len(adjacentPairs) + 1
    ret = [0] * n

    # 找到首或尾
    for key, arr in mp.items():
        if len(arr) == 1:
            ret[0] = key
            break

    ret[1] = mp[ret[0]][0]
    for i in range(2, n):
        adj = mp[ret[i - 1]]
        ret[i] = adj[1] if adj[0] == ret[i - 2] else adj[0]

    return ret
