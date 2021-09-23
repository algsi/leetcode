"""
581. shortest unsorted continuous subarray

https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/

最短无序连续子数组
"""

from typing import List


def find_unsorted_subarray(nums: List[int]) -> int:
    """
    sort

    Complexity Analysis
    time complexity: O(nlogn)
    space complexity: O(n)
    """
    if not nums:
        return 0

    sorted_nums = sorted(nums)
    n = len(nums) - 1
    start, end = n, 0
    for i in range(n):
        if sorted_nums[i] != nums[i]:
            start = min(start, i)
            end = max(end, i)

    return end - start + 1 if end - start >= 0 else 0


if __name__ == '__main__':
    find_unsorted_subarray([2, 6, 4, 8, 10, 9, 15])
