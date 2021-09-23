"""
1480. running sum of 1d array

https://leetcode.com/problems/running-sum-of-1d-array/
https://leetcode-cn.com/problems/running-sum-of-1d-array/

一维数组的动态和
"""

from typing import List


def running_sum(nums: List[int]) -> List[int]:
    n = len(nums)
    for i in range(1, n):
        nums[i] += nums[i - 1]
    return nums
