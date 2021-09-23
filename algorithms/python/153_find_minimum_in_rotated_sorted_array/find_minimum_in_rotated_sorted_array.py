"""
153. find minimum in rotated sorted array

寻找旋转排序数组中的最小值（你可以假设数组中不存在重复元素）

see also: 154. find minimum in rotated sorted array II
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
    # if the last element is greater than the first element then there is no rotation.
    if nums[hi] > nums[0]:
        return nums[0]

    # binary search way
    while lo <= hi:
        # the mid element
        mid = (hi - lo) // 2 + lo
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        if nums[mid - 1] > nums[mid]:
            return nums[mid]
        if nums[mid] > nums[0]:
            lo = mid + 1
        else:
            hi = mid - 1


if __name__ == '__main__':
    nums = [1, 2, 3]
    r = find_min(nums)
    print(r)
