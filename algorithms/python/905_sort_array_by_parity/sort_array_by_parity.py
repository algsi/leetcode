"""
905. sort array by parity

按奇偶排序数组
"""

from typing import List


class Solution:
    def sort_array_by_parity(self, A: List[int]) -> List[int]:
        self.partition(A, 0, len(A) - 1)
        return A

    def partition(self, arr: List[int], lo, hi):
        i, j = lo - 1, hi + 1
        while True:
            i += 1
            j -= 1
            while arr[i] % 2 == 0:
                i += 1
                if i >= hi:
                    break
            while arr[j] % 2 == 1:
                j -= 1
                if j <= lo:
                    break

            if i >= j:
                break

            arr[i], arr[j] = arr[j], arr[i]
