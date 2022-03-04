"""
912. sort an array

https://leetcode.com/problems/sort-an-array/
https://leetcode-cn.com/problems/sort-an-array/

排序数组
"""

from typing import List
import random


class Solution:
    """
    快速排序 quick sort
    """

    def sort_array(self, nums: List[int]) -> List[int]:
        self.random_partition(nums, 0, len(nums) - 1)
        return nums

    @staticmethod
    def random_partition(nums: List[int], left: int, right: int):
        if left >= right:
            return
        pivot_id = random.randint(left, right)
        pivot = nums[pivot_id]
        nums[pivot_id], nums[right] = nums[right], nums[pivot_id]
        i = left - 1
        for j in range(left, right + 1):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        i += 1
        nums[i], nums[right] = nums[right], nums[i]
        Solution.random_partition(nums, left, i - 1)
        Solution.random_partition(nums, i + 1, right)
