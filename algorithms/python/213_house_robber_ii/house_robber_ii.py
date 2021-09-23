"""
213. House Robber II

打家劫舍 II
"""

from typing import List


def rob(nums: List[int]) -> int:
    """
    动态规划
    因为首尾的特殊性，因此在 198 的前提下做两次动态规划，分成第一个房子偷与不偷的情况。
    如果偷第一个房子，那么最后一个房子一定不能偷，如果不偷第一个房子，那么不考虑第一个房子，剩下的正常考虑
    """

    def my_rob(nums: List[int]) -> int:
        """
        函数闭包
        """
        prev_max, cur_max = 0, 0
        for i in range(len(nums)):
            temp = cur_max
            cur_max = max(cur_max, prev_max + nums[i])
            prev_max = temp

        return cur_max

    return max(my_rob(nums[:-1]), my_rob(nums[1:])) if len(nums) != 1 else nums[0]
