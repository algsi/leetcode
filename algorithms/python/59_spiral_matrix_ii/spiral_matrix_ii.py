"""
59. Spiral Matrix II

https://leetcode-cn.com/problems/spiral-matrix-ii/

螺旋矩阵 II
"""

from typing import List


def generate_matrix(n: int) -> List[List[int]]:
    """
    和 54 题（spiral matrix）如出一辙，只需要定义好边界即可
    """
    if n == 1:
        return [[1]]

    # init
    matrix = [[0] * n for _ in range(n)]
    num = 1
    # 定义上下左右的边界
    top, bottom, left, right = 0, n - 1, 0, n - 1
    while True:
        # top
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1
        if top > bottom:
            break

        # right
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
        if right < left:
            break

        # bottom
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1
        if top > bottom:
            break

        # left
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1
        if right < left:
            break

    return matrix
