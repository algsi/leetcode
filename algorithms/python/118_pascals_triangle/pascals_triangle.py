"""
118. pascals triangle

https://leetcode.com/problems/pascals-triangle/
https://leetcode-cn.com/problems/pascals-triangle/

杨辉三角
"""

from typing import List


class Solution:
    def generate(self, num_rows: int) -> List[List[int]]:
        if num_rows == 0:
            return []
        output = [[0] * (i + 1) for i in range(num_rows)]
        output[0][0] = 1
        for i in range(1, num_rows):
            level = output[i]
            level[0] = 1
            for j in range(1, i):
                level[j] = output[i - 1][j - 1] + output[i - 1][j]
            level[i] = 1

        return output
