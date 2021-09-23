"""
35. search insert position

搜索插入位置
"""

from typing import List


def search_insert(nums: List[int], target: int) -> int:
    """
    binary search
    """
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (hi - lo) // 2 + lo
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return hi + 1
