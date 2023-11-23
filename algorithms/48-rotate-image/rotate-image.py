from typing import List


def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.

    用翻转代替旋转：先水平反转，再对角线反转
    """
    n = len(matrix)
    for idx in range(n // 2):
        matrix[idx], matrix[n - 1 - idx] = matrix[n - 1 - idx], matrix[idx]

    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
