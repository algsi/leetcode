"""
198. House Robber

打家劫舍
"""

from typing import List


def rob(nums: List[int]) -> int:
    """
    动态规划
    """
    prev_max, cur_max = 0, 0
    for i in range(len(nums)):
        temp = cur_max
        cur_max = max(cur_max, prev_max + nums[i])
        prev_max = temp

    return cur_max
