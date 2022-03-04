"""
64. minimum path sum

https://leetcode.com/problems/minimum-path-sum/submissions/
https://leetcode-cn.com/problems/minimum-path-sum/submissions/

最小路径和
"""

from typing import List


def min_path_sum(grid: List[List[int]]) -> int:
    """
    dynamic programming
    """
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    # initialize
    dp[0][0] = grid[0][0]
    for j in range(1, n):
        dp[0][j] = grid[0][j] + dp[0][j - 1]

    for i in range(1, m):
        for j in range(n):
            if j == 0:
                dp[i][j] = dp[i - 1][j] + grid[i][j]
                continue
            dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]


def min_path_sum_2(grid: List[List[int]]) -> int:
    """
    dynamic programming + space optimization
    """
    m, n = len(grid), len(grid[0])
    dp = [0] * n

    # initialize
    dp[0] = grid[0][0]
    for j in range(1, n):
        dp[j] = grid[0][j] + dp[j - 1]

    for i in range(1, m):
        for j in range(n):
            if j == 0:
                dp[j] = dp[j] + grid[i][j]
                continue
            dp[j] = grid[i][j] + min(dp[j], dp[j - 1])
    return dp[-1]


def min_path_sum_3(grid: List[List[int]]) -> int:
    """
    dynamic programming

    如果没有特殊要求，可以原地DP，利用原数组空间
    """
    pass
