"""
674. longest continuous increasing subsequence

https://leetcode.com/problems/longest-continuous-increasing-subsequence/
https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence/

最长连续递增序列
"""

from typing import List


def find_length_of_LCIS(nums: List[int]) -> int:
    """
    贪心算法
    """
    ans = 0
    n = len(nums)
    start = 0
    for i in range(n):
        if i > 0 and nums[i] <= nums[i - 1]:
            start = i
        ans = max(ans, i - start + 1)
    return ans
