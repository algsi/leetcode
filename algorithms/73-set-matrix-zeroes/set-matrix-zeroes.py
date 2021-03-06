"""
73. set matrix zeroes

https://leetcode.com/problems/set-matrix-zeroes/
https://leetcode-cn.com/problems/set-matrix-zeroes/

矩阵置零
"""

from typing import List


def set_zeroes(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    m, n = len(matrix), len(matrix[0])
    flag_col0 = False

    for i in range(m):
        if matrix[i][0] == 0:
            flag_col0 = True
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0

    for i in range(m - 1, -1, -1):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
        if flag_col0:
            matrix[i][0] = 0
