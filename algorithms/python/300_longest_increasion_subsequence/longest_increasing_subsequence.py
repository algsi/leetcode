"""
300. longest increasing subsequence

最长上升子序列（这里的上升是"严格上升"）
"""

from typing import List


def longest_increasing_subsequence(nums: List[int]) -> int:
    """
    dynamic programming

    Complexity Analysis
    time complexity: O(N^2)
    space complexity: O(N)
    """
    if not nums:
        return 0

    n = len(nums)
    # dp[i] 表示以位置 i 结尾的上升子序列的长度，注意 nums[i] 必须被选取。
    dp = [0] * n
    dp[0] = 1
    result = 1
    for i in range(1, n):
        dp[i] = 1
        for j in range(0, i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])
        result = max(result, dp[i])

    return result


def longest_increasing_subsequence_2(nums: List[int]) -> int:
    """
    贪心 + 二分查找
    """
    if not nums:
        return 0

    dp = []
    for n in nums:
        if not dp or n > dp[-1]:
            dp.append(n)
        else:
            lo, hi = 0, len(dp) - 1
            loc = hi
            while lo <= hi:
                mid = (lo + hi) // 2
                if dp[mid] >= n:
                    loc = mid
                    hi = mid - 1
                else:
                    lo = mid + 1
            dp[loc] = n

    return len(dp)
