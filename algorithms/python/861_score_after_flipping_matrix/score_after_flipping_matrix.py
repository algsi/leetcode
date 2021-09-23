"""
861. score after flipping matrix

https://leetcode.com/problems/score-after-flipping-matrix/
https://leetcode-cn.com/problems/score-after-flipping-matrix/

翻转矩阵后的得分
"""

from typing import List


class Solution:
    """
    贪心算法 + 位运算
    """

    def matrix_score(self, A: List[List[int]]) -> int:
        m = len(A)
        n = len(A[0])
        # 第一列
        output = m * (1 << (n - 1))
        # 先遍历列
        for j in range(1, n):
            n_one = 0  # 当前列 1 的数量
            for row in A:
                if row[0] == 1:
                    # 行无需反转
                    n_one += row[j]
                else:
                    # 行需要反转
                    n_one += (1 - row[j])
            k = max(n_one, m - n_one)
            output += k * (1 << (n - j - 1))

        return output
