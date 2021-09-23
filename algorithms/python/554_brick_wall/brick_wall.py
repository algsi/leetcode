"""
554. brick wall

https://leetcode.com/problems/brick-wall/
https://leetcode-cn.com/problems/brick-wall/

砖墙
"""

from typing import List


def least_bricks(wall: List[List[int]]) -> int:
    """
    哈希表
    """
    mp = dict()
    for widths in wall:
        sum = 0

        # 最后一个砖缝不能取
        for width in widths[:-1]:
            sum += width
            mp[sum] = mp.get(sum, 0) + 1

    max_cnt = 0
    for value in mp.values():
        max_cnt = max(max_cnt, value)

    return len(wall) - max_cnt
