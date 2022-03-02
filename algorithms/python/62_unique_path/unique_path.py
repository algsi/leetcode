"""
62. unique path

不同路径
"""


def unique_paths(m: int, n: int) -> int:
    """
    dynamic programming
    """
    dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]
