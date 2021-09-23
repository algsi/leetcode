"""
329. longest increasing path in a matrix

https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix/

矩阵中的最长递增路径
"""

from typing import List


class Solution:
    """
    深度优先搜索 + 记忆化

    complexity analysis
    time complexity: O(mn)
    space complexity: O(mn)
    """
    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def longest_increasing_path(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        ans = 0
        rows, columns = len(matrix), len(matrix[0])
        memo = [[0] * columns for _ in range(rows)]  # memory

        def dfs(row: int, column: int) -> int:
            if memo[row][column]:
                return memo[row][column]
            best = 1
            for dx, dy in Solution.DIRS:
                new_row, new_column = row + dx, column + dy
                if 0 <= new_row < rows \
                        and 0 <= new_column < columns \
                        and matrix[new_row][new_column] > matrix[row][column]:
                    best = max(best, dfs(new_row, new_column) + 1)
            memo[row][column] = best
            return best

        for i in range(rows):
            for j in range(columns):
                ans = max(ans, dfs(i, j))
        return ans
