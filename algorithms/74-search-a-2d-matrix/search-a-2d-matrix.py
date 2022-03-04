"""
74. search a 2d matrix

https://leetcode.com/problems/search-a-2d-matrix/
https://leetcode-cn.com/problems/search-a-2d-matrix/

搜索二维矩阵
"""

from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    """
    binary search
    """
    m = len(matrix)
    n = len(matrix[0])
    low, high = 0, m * n - 1
    while low <= high:
        mid = (high - low) // 2 + low

        # 将一维坐标映射到二维
        x = matrix[mid // n][mid % n]
        if x < target:
            low = mid + 1
        elif x > target:
            high = mid - 1
        else:
            return True
    return False


if __name__ == '__main__':
    p1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    p2 = 3
    search_matrix(p1, p2)
