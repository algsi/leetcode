"""
1030. matrix cell in distance order

https://leetcode.com/problems/matrix-cells-in-distance-order/
https://leetcode-cn.com/problems/matrix-cells-in-distance-order/
"""
from typing import List


class Solution1:
    """
    直接排序

    时间复杂度：O(RClog(RC))，存储所有点时间复杂度 O(RC)，排序时间复杂度 O(RClog(RC))。
    空间复杂度：O(log(RC))，即为排序需要使用的栈空间，不考虑返回值的空间占用。
    """

    def all_cells_dist_order(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        ret = [[i, j] for i in range(R) for j in range(C)]
        ret.sort(key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))
        return ret


class Solution2:
    """
    几何法遍历
    """

    def all_cells_dist_order(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        max_dist = max(r0, R - r0 - 1) + max(c0, C - c0 - 1)
        row, col = r0, c0
        ret = [[row, col]]
        for dist in range(1, max_dist):
            row -= 1
            for i, (dr, dc) in enumerate(dirs):
                while (i % 2 == 0 and row != r0) or (i % 2 != 0 and col != c0):
                    if 0 <= row < R and 0 <= col < C:
                        ret.append([row, col])
                    row += dr
                    col += dc

        return ret
