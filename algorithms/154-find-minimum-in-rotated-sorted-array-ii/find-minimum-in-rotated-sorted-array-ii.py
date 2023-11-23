"""
154. find minimum in rotated sorted array II

寻找旋转排序数组中的最小值 II

see also: 153. find minimum in rotated sorted array
"""

from typing import List


def find_min(nums: List[int]) -> int:
    """
    binary search
    """
    n = len(nums)

    # if the list has just one element then return the element
    if n == 1:
        return nums[0]

    lo, hi = 0, n - 1
    # if the last element is not less than the first element then there is no rotation.
    if nums[hi] >= nums[0]:
        return nums[0]

    # binary search way
    while lo < hi:
        pivot = lo + (hi - lo) // 2
        if nums[pivot] < nums[hi]:
            hi = pivot
        elif nums[pivot] > nums[hi]:
            lo = pivot + 1
        else:
            hi -= 1
    return nums[lo]
