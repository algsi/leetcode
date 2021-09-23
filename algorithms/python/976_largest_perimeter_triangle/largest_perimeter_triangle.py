"""
976. largest perimeter triangle

https://leetcode.com/problems/largest-perimeter-triangle/
https://leetcode-cn.com/problems/largest-perimeter-triangle/

三角形的最大周长
"""

from typing import List


class Solution:
    def largest_perimeter(self, A: List[int]) -> int:
        A.sort()
        n = len(A)
        for i in range(n - 1, 1, -1):
            if A[i - 1] + A[i - 2] > A[i]:
                return A[i - 2] + A[i - 1] + A[i]
        return 0
