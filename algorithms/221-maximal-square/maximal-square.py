"""
221. maximal square

最大正方形
"""

from typing import List


def maximal_square(matrix: List[List[str]]) -> int:
    """
    DP

    dp(i,j) 表示以 (i,j) 为右下角，且只包含 1 的正方形的边长最大值。

    dp(i,j)=min(dp(i−1,j),dp(i−1,j−1),dp(i,j−1))+1
    dp(i,j)=1, if i=0 or j=0
    """

    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0

    max_side = 0
    rows, columns = len(matrix), len(matrix[0])
    dp = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == '1':
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                max_side = max(max_side, dp[i][j])

    return max_side ** 2
