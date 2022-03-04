"""搜索二维矩阵 II
"""

from typing import List
import bisect


def search_matrix_v1(matrix: List[List[int]], target: int) -> bool:
    """
    二分查找
    对每一行使用一次二分查找
    """
    for row in matrix:
        idx = bisect.bisect_left(row, target)
        if idx < len(row) and row[idx] == target:
            return True
    return False
