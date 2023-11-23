"""
34. find first and last position of element in sorted array

https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/

在排序数组中查找元素的第一个和最后一个位置
"""

from typing import List


class Solution:
    def search_range(self, nums: List[int], target: int) -> List[int]:
        left_idx = self.bisect(nums, target, True)
        right_idx = self.bisect(nums, target, False) - 1
        if left_idx <= right_idx < len(nums) and nums[left_idx] == target and nums[right_idx] == target:
            return [left_idx, right_idx]
        return [-1, -1]

    @staticmethod
    def bisect(nums: List[int], target: int, left: bool) -> bool:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if left:
                if nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            else:
                if target < nums[mid]:
                    hi = mid
                else:
                    lo = mid + 1
        return lo
