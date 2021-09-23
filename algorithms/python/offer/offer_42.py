"""
剑指 Offer 42. 连续子数组的最大和

https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/
"""

from typing import List


def max_sub_array(nums: List[int]) -> int:
    """
    动态规划
    """
    cur = nums[0]
    ans = nums[0]
    for num in nums[1:]:
        cur = max(cur + num, num)
        ans = max(ans, cur)
    return ans
