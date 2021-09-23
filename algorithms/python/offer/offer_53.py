"""
剑指 Offer 53 - I. 在排序数组中查找数字 I

https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/
"""

import bisect
from typing import List


def search(nums: List[int], target: int) -> int:
    """
    使用内置的 bisect 模块
    """
    left = bisect.bisect_left(nums, target)
    right = bisect.bisect_right(nums, target)
    return right - left
