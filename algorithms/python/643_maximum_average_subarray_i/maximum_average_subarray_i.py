"""
643. maximum average subarray i

https://leetcode.com/problems/maximum-average-subarray-i/
https://leetcode-cn.com/problems/maximum-average-subarray-i/

子数组最大平均数 I
"""

from typing import List


def find_max_average(nums: List[int], k: int) -> float:
    """
    滑动窗口
    """
    max_total = total = sum(nums[:k])
    n = len(nums)
    for i in range(k, n):
        total = total - nums[i - k] + nums[i]
        max_total = max(max_total, total)
    return max_total / k
