"""
922. sort array by parity ii

https://leetcode.com/problems/sort-array-by-parity-ii/
https://leetcode-cn.com/problems/sort-array-by-parity-ii/

按奇偶排序数组 II
"""
from typing import List


class Solution:
    """
    dual pointer
    """

    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even, odd = 0, 1
        n = len(A)
        while True:
            # step = 2
            while even < n - 1 and A[even] & 1 == 0:
                even += 2
            if n - 1 <= even:
                return A
            while odd < n and A[odd] & 1 == 1:
                odd += 2
            if n <= odd:
                return A
            A[odd], A[even] = A[even], A[odd]
            odd += 2
            even += 2
