"""
977. squares of a sorted array

https://leetcode.com/problems/squares-of-a-sorted-array/
https://leetcode-cn.com/problems/squares-of-a-sorted-array/
"""

from typing import List


class Solution:
    """
    dual pointer

    双指针，从数组两端往中间逼近

    complexity analysis
    time complexity: O(n)
    space complexity: O(1)
    """

    def sortedSquares(self, A: List[int]) -> List[int]:
        n = len(A)
        output = [0] * n
        i, j = 0, n - 1
        index = j
        while i <= j:
            if abs(A[i]) >= abs(A[j]):
                output[index] = A[i] ** 2
                i += 1
            else:
                output[index] = A[j] ** 2
                j -= 1
            index -= 1
        return output
