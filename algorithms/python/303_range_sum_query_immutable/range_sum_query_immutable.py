"""
303. range sum query immutable

https://leetcode-cn.com/problems/range-sum-query-immutable

区域和检索 - 数组不可变
"""

from typing import List


class NumArray:
    """
    利用前缀和做缓存
    """

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.prefix_sum = [0] * (n + 1)
        for i in range(n):
            self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.prefix_sum[j + 1] - self.prefix_sum[i]

