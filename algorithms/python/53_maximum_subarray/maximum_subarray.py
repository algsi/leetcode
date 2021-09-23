"""
53. maximum subarray

最大子序和
"""

from typing import List


def max_subarray(nums: List[int]) -> int:
    """
    动态规划
    设 dp[i] 表示为以 i 下标所在元素结尾的最大子序和，那么 dp[i]=max(num[i], dp[i-1]+nums[i])
    因为我们只需要保留前一个状态，所以也无需数组。
    """
    ans = nums[0]
    prev = ans

    n = len(nums)
    for i in range(1, n):
        prev = max(prev + nums[i], nums[i])
        if prev > ans:
            ans = prev

    return ans
