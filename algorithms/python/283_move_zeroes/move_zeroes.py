"""
283. move zeroes

https://leetcode.com/problems/move-zeroes/
https://leetcode-cn.com/problems/move-zeroes/
"""

from typing import List


class Solution:
    """
    dual pointer

    左指针指向当前已经处理好的序列的尾部，右指针指向待处理序列的头部。
    """

    def move_zeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        n = len(nums)
        left, right = 0, 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
