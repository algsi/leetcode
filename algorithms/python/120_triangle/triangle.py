"""
120. triangle

https://leetcode.com/problems/triangle/
https://leetcode-cn.com/problems/triangle/

三角形最小路径和
"""

from typing import List


def minimum_total(triangle: List[List[int]]) -> int:
    """
    dynamic programming

    一定要自顶向下，一定要经过定点

    自顶向下动态规划
    """

    # initialize
    dp = [[0] * len(i) for i in triangle]
    dp[0][0] = triangle[0][0]
    mark = 1
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j > mark:
                # 路径不连续，剪枝
                continue
            if j >= len(triangle[i - 1]):
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
                continue

            dp[i][j] = dp[i - 1][j]
            if j - 1 >= 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
            dp[i][j] += triangle[i][j]

        mark += 1

    return min(dp[-1])


def minimum_total_2(triangle: List[List[int]]) -> int:
    """
    dynamic programming

    从三角形的底部开始转移，到顶部结束（自底向上）
    """
    pass


def minimum_total_3(triangle: List[List[int]]) -> int:
    """
    dynamic programming

    直接在给定的三角形数组上进行状态转移，不使用额外的空间。（in-place）
    """
    mark = 1
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j > mark:
                # 路径不连续，剪枝
                continue
            if j >= len(triangle[i - 1]):
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i][j]
                continue

            tmp = triangle[i - 1][j]
            if j - 1 >= 0:
                tmp = min(triangle[i - 1][j], triangle[i - 1][j - 1])
            triangle[i][j] += tmp

        mark += 1

    return min(triangle[-1])


if __name__ == '__main__':
    r = minimum_total_3([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
    print(r)
