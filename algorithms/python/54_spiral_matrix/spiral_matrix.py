"""
54. Spiral Matrix

https://leetcode.com/problems/spiral-matrix/

螺旋打印矩阵
"""

from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:
    """
    不需要记录已经走过的路径

    首先设定上下左右边界
    其次向右移动到最右，此时第一行因为已经使用过了，可以将其从图中删去，体现在代码中就是重新定义上边界
    判断若重新定义后，上下边界交错，表明螺旋矩阵遍历结束，跳出循环，返回答案
    若上下边界不交错，则遍历还未结束，接着向下向左向上移动，操作过程与第一，二步同理<
    不断循环以上步骤，直到某两条边界交错，跳出循环，返回答案
    """
    if not matrix:
        return []

    m, n = len(matrix), len(matrix[0])
    top, bottom, left, right = 0, m - 1, 0, n - 1
    ans = []
    while True:
        # top
        for i in range(left, right + 1):
            ans.append(matrix[top][i])
        top += 1
        if top > bottom:
            break

        # right
        for i in range(top, bottom + 1):
            ans.append(matrix[i][right])
        right -= 1
        if right < left:
            break

        # bottom
        for i in range(right, left - 1, -1):
            ans.append(matrix[bottom][i])
        bottom -= 1
        if top > bottom:
            break

        # left
        for i in range(bottom, top - 1, -1):
            ans.append(matrix[i][left])
        left += 1
        if right < left:
            break

    return ans
