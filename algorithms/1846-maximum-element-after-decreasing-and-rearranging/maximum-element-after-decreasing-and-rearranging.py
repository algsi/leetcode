"""
1846. maximum element after decreasing and rearranging

https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/
https://leetcode-cn.com/problems/maximum-element-after-decreasing-and-rearranging/

减小和重新排列数组后的最大元素
"""

from typing import List


def maximum_element_after_decrementing_and_rearranging(arr: List[int]) -> int:
    n = len(arr)
    arr.sort()
    arr[0] = 1
    for i in range(1, n):
        arr[i] = min(arr[i], arr[i - 1] + 1)
    return arr[n - 1]
