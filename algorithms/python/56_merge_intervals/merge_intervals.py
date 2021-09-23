"""
LeetCode 56: 合并区间

https://leetcode-cn.com/problems/merge-intervals/

如果我们按照区间的左端点排序，那么在排完序的列表中，可以合并的区间一定是连续的。
"""

from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    # sort
    intervals.sort(key=lambda x: x[0])
    merged = []

    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # merge
            merged[-1][1] = max(interval[1], merged[-1][1])

    return merged
