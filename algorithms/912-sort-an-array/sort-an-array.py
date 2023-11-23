"""
912. sort an array

https://leetcode.com/problems/sort-an-array/
https://leetcode-cn.com/problems/sort-an-array/

排序数组
"""

from ast import Num
from operator import le
from tkinter import N
from typing import List
import random


class Solution:
    """
    快速排序 quick sort
    """

    def sort_array(self, nums: List[int]) -> List[int]:
        self.randomized_quicksort(nums, 0, len(nums) - 1)
        return nums

    def randomized_partition(self, nums: List[int], l: int, r: int):
        pivot = random.randint(l, r)
        nums[pivot], nums[r] = nums[r], nums[pivot]
        i = l - 1
        for j in range(l, r):
            if nums[j] < nums[r]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        i += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i

    def randomized_quicksort(self, nums, l, r):
        if r <= l:
            return
        mid = self.randomized_partition(nums, l, r)
        self.randomized_quicksort(nums, l, mid - 1)
        self.randomized_quicksort(nums, mid + 1, r)


class SolutionV2:
    """
    归并排序 merge sort
    """

    def sort_array(self, nums: List[int]) -> List[int]:
        self.merge_sort(nums, 0, len(nums) - 1)
        return nums

    def merge_sort(self, nums: List[int], left: int, right: int):
        if left == right:
            return
        mid = left + (right - left) // 2
        self.merge_sort(nums, left, mid)
        self.merge_sort(nums, mid + 1, right)
        i, j = left, mid + 1
        tmp = []
        while i <= mid or j <= right:
            if i > mid or (j <= right and nums[j] < nums[i]):
                tmp.append(nums[j])
                j += 1
            else:
                tmp.append(nums[i])
                i += 1
        nums[left:right + 1] = tmp
