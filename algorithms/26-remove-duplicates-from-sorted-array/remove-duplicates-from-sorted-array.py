"""
26. remove duplicates from sorted array

https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array

删除排序数组中的重复项
"""

from typing import List


def remove_duplicates(nums: List[int]) -> int:
    """
    dual pointer(快慢指针)

    Complexity Analysis
    time complexity: O(N)
    space complexity: O(1)
    """

    if not nums:
        return 0

    n = len(nums)
    fast = slow = 1
    while fast < n:
        if nums[fast] != nums[fast - 1]:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1

    return slow
